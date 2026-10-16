"""Independent regression tests for portable Chapter II receiving formulas.

These tests check finite examples and source-reported quantities; they do not
replace the retained scientific certificates or claim an experimental result.
"""
from fractions import Fraction as F
import math
import unittest

from sam_chapter2 import (
    Interval, residual_certificate, quadratic_error_envelope,
    decaying_error_envelope, quadratic_remainder_bound,
    radial_green, radial_dirichlet_operator, radial_shell_solution,
    correlated_phase_bounds, independent_band_threshold, actual_clock_phase,
    SamplingPlan, shot_count, log_bounds, difference_hankel, determinant3,
    difference_minor, determinant_rejection_threshold,
    two_record_perturbation_bound, paid_reference_protocol, unwrap_reference_phase,
)


class ExactIntervals(unittest.TestCase):
    def test_signed_interval_products_enclose_all_endpoints(self):
        a, b = Interval(-3, 2), Interval(-2, 5)
        self.assertEqual(a*b, Interval(-15, 10))
        self.assertEqual(3-a, Interval(1, 6))
        self.assertEqual(a+F(1, 2), Interval(F(-5, 2), F(5, 2)))

    def test_floating_point_and_reversed_endpoints_are_rejected(self):
        with self.assertRaises(TypeError):
            Interval(0.1, 1)
        with self.assertRaises(TypeError):
            Interval(True, 1)
        with self.assertRaises(ValueError):
            Interval(2, 1)


class OriginalGramMemory(unittest.TestCase):
    def test_nonorthonormal_example_has_physical_norm_five_not_forty(self):
        # A=[[2,1,1],[1,3,2],[1,2,5]], b=(2e1,3e2). Only e3 is hidden.
        cert = residual_certificate([[4, 0], [0, 9]], [[8, 6], [6, 27]],
                                    [[24, 42], [42, 126]])
        self.assertEqual(cert.residual, ((F(4), F(12)), (F(12), F(36))))
        self.assertEqual(cert.rank, 1)
        self.assertFalse(cert.is_closed)
        self.assertEqual(cert.memory_norm_upper, 5)
        self.assertEqual(cert.generalized_rayleigh([F(1, 2), F(2, 3)]), 5)
        self.assertNotEqual(sum(cert.residual[i][i] for i in range(2)),
                            cert.memory_norm_upper)

    def test_basis_rescaling_keeps_closure_and_normalized_memory(self):
        first = residual_certificate([[1]], [[2]], [[5]])
        rescaled = residual_certificate([[9]], [[18]], [[45]])
        self.assertEqual(first.normalized_trace, rescaled.normalized_trace)
        self.assertEqual(first.rank, rescaled.rank)
        closed = residual_certificate([[9]], [[18]], [[36]])
        self.assertTrue(closed.is_closed)
        self.assertEqual(closed.normalized_trace, 0)

    def test_multidirectional_trace_is_an_upper_bound_not_an_exact_norm(self):
        cert = residual_certificate([[1, 0], [0, 1]], [[1, 0], [0, 1]],
                                    [[2, 0], [0, 3]])
        self.assertEqual(cert.rank, 2)
        self.assertEqual(cert.memory_norm_upper, 3)
        self.assertEqual(cert.generalized_rayleigh([0, 1]), 2)

    def test_exact_evolution_obeys_double_integral_bound(self):
        # For A=[[2,1],[1,2]], compressed evolution=e^-2t cosh(t), B=2.
        for t in (F(1, 100), F(1, 10), F(1), F(4)):
            x = float(t)
            defect = math.exp(-2*x)*(math.cosh(x)-1)
            bound = decaying_error_envelope(t, 1, 1)
            self.assertLessEqual(defect, bound)
            self.assertLessEqual(abs(defect-float(t*t/2)),
                                 float(quadratic_remainder_bound(t, 1, 3)))
        self.assertEqual(quadratic_error_envelope(F(1, 10), 5), F(1, 40))

    def test_invalid_moment_data_and_vectors_fail(self):
        cases = (
            ([[0]], [[0]], [[0]]),
            ([[1]], [[2]], [[3]]),
            ([[1, 0], [0, 1]], [[1, 1], [0, 1]], [[1, 0], [0, 1]]),
            ([[1]], [[1, 0], [0, 1]], [[1]]),
            ([[1, 0], [0, 1]], [[0, 0], [0, 0]], [[0, 1], [1, 0]]),
        )
        for args in cases:
            with self.subTest(args=args), self.assertRaises(ValueError):
                residual_certificate(*args)
        cert = residual_certificate([[1]], [[2]], [[5]])
        for vector in ([0], [1, 1]):
            with self.assertRaises(ValueError):
                cert.generalized_rayleigh(vector)
        with self.assertRaises(ValueError):
            quadratic_error_envelope(-1, 2)
        with self.assertRaises(ValueError):
            decaying_error_envelope(1, 2, -1)


class RadialReceiver(unittest.TestCase):
    def test_green_is_inverse_of_incidence_conductance_operator(self):
        for L in (2, 3, 7, 10):
            h, k = radial_green(L), radial_dirichlet_operator(L)
            for i in range(L-1):
                for j in range(L-1):
                    self.assertEqual(sum(k[i][q]*h[q][j] for q in range(L-1)),
                                     F(i == j))

    def test_mass_flux_including_outer_boundary_and_reference_shift(self):
        masses = (F(1, 10), F(1, 5), F(7, 10))
        solution = radial_shell_solution(masses, F(1, 50))
        for i, flux in enumerate(solution.flux, 1):
            self.assertEqual(flux, F(1, 50)*sum(masses[:i]))
        self.assertEqual(solution.infinity_shift, F(1, 200))
        for i in range(len(masses)-1):
            self.assertEqual(solution.lift[i]-solution.lift[i+1],
                             solution.isolated_lift[i]-solution.isolated_lift[i+1])
        self.assertLess(solution.reduced_binding, 0)

    def test_single_shell_half_self_binding_and_mass_scaling(self):
        single = radial_shell_solution([3], F(1, 20))
        self.assertEqual(single.lift, (F(3, 40),))
        self.assertEqual(single.isolated_lift, (F(3, 20),))
        self.assertEqual(single.reduced_binding, F(-9, 4))
        doubled = radial_shell_solution([6], F(1, 20))
        self.assertEqual(doubled.reduced_binding, 4*single.reduced_binding)
        self.assertEqual(doubled.lift[0], 2*single.lift[0])

    def test_invalid_geometry_mass_and_scale_fail(self):
        for L in (1, True, F(3, 2)):
            with self.assertRaises(ValueError):
                radial_green(L)
        for masses, scale in (([], 1), ([-1, 2], 1), ([1], 0)):
            with self.assertRaises(ValueError):
                radial_shell_solution(masses, scale)


class EnsembleMeasurement(unittest.TestCase):
    def test_certified_log_enclosures_nest_and_bound_known_powers(self):
        lo, hi = log_bounds(2, 16)
        self.assertLess(lo, F("0.693147180559945309417232121458176568"))
        self.assertGreater(hi, F("0.693147180559945309417232121458176568"))
        fine_lo, fine_hi = log_bounds(2, 32)
        self.assertLessEqual(lo, fine_lo)
        self.assertLessEqual(fine_hi, hi)
        self.assertEqual(log_bounds(1), (F(0), F(0)))
        lo8, hi8 = log_bounds(8, 16)
        self.assertEqual((lo8, hi8), (3*lo, 3*hi))

    def test_protected_coherence_shot_budget_reproduces_chapter(self):
        plan = shot_count(8, F(3, 500), F(1, 100), outcome_radius_squared=2)
        self.assertEqual(plan.shots_per_mean, 819751)
        self.assertEqual(plan.total_fresh_preparations, 6558008)
        self.assertTrue(plan.sufficient)
        previous = SamplingPlan(8, 819750, F(3, 500), F(1, 100), F(2))
        self.assertFalse(previous.sufficient)

    def test_reference_protocol_preserves_conservative_retained_shot_budget(self):
        retained = SamplingPlan(882, 26624, F(1, 32), F(1, 100), F(1))
        self.assertTrue(retained.sufficient)
        self.assertEqual(retained.total_fresh_preparations, 23482368)
        # The API calculates the exact minimum of this sufficient inequality;
        # the chapter intentionally uses the larger, simple certified count.
        minimum = shot_count(882, F(1, 32), F(1, 100))
        self.assertEqual(minimum.shots_per_mean, 24741)
        self.assertLess(minimum.shots_per_mean, retained.shots_per_mean)

    def test_sampling_budget_scales_with_radius_and_fresh_copy_count(self):
        pauli = shot_count(8, F(1, 100), F(1, 100))
        protected = shot_count(8, F(1, 100), F(1, 100), outcome_radius_squared=2)
        self.assertGreaterEqual(protected.shots_per_mean, 2*pauli.shots_per_mean-1)
        self.assertGreater(shot_count(8, F(1, 200), F(1, 100)).shots_per_mean,
                           pauli.shots_per_mean)

    def test_two_state_cosine_record_has_zero_three_by_three_minors(self):
        # Exact recurrence for cos(n*theta), cos(theta)=3/5; constant removed.
        cosines = [F(1), F(3, 5)]
        for _ in range(6):
            cosines.append(F(6, 5)*cosines[-1]-cosines[-2])
        means = [F(2, 7)+F(1, 3)*c for c in cosines]
        self.assertEqual(difference_minor(means), 0)
        self.assertEqual(difference_minor(means, (0, 1, 2)), 0)
        self.assertEqual(len(difference_hankel(means)), 4)

    def test_non_two_state_control_and_determinant_noise_threshold(self):
        # A generic polynomial control is deliberately outside the two-state
        # comparison class; it checks the decision machinery, not SAM dynamics.
        record = [F(k**3) for k in range(8)]
        self.assertNotEqual(difference_minor(record), 0)
        self.assertEqual(two_record_perturbation_bound(F(1, 100)), F("2.996352"))
        self.assertLess(two_record_perturbation_bound(F(1, 100)),
                        F("5.318723982743267"))
        self.assertEqual(determinant_rejection_threshold(F(1, 100), 2),
                         36*F(1, 100)*F(101, 50)**2)
        self.assertEqual(determinant3([[1, 2, 0], [0, 1, 3], [2, 0, 1]]), 13)

    def test_invalid_sampling_and_hankel_inputs_fail(self):
        for args in ((0, "0.1", "0.01"), (8, 0, "0.01"), (8, "0.1", 1)):
            with self.assertRaises(ValueError):
                shot_count(*args)
        with self.assertRaises(ValueError):
            difference_hankel([0]*7)
        with self.assertRaises(ValueError):
            difference_minor([0]*8, (0, 0, 3))
        with self.assertRaises(ValueError):
            determinant_rejection_threshold(-1, 2)
        with self.assertRaises(ValueError):
            SamplingPlan(8, 0, F(1, 100), F(1, 100), F(1))


class PaidReference(unittest.TestCase):
    @staticmethod
    def protocol():
        return paid_reference_protocol(
            Interval("0.917629340281369063", "0.917632830384309734"),
            Interval("0.158555895876030285", "0.158555895876030286"),
            Interval("3.14159265358979323846264338327950288419716939937510",
                     "3.14159265358979323846264338327950288419716939937511"),
            Interval("10.10565104318054", "10.10565104318055"),
            Interval("9.81032032323410", "9.81032032323411"))

    def test_wait_keeps_reference_on_while_original_clock_keeps_advancing(self):
        protocol = self.protocol()
        wait = next(s for s in protocol.intervals if s.name == "source_wait")
        self.assertEqual(wait.ledger_phase_change, Interval.point(0))
        self.assertLess(wait.reference_energy.upper, 0)
        self.assertLess(wait.beta_change.upper, -2*F("3.1415926535897933"))
        before, after = protocol.events[3:5]
        theta_before = actual_clock_phase("0.0000034901029295", "0.0000034901029346",
                                         before.source_time)
        theta_after = actual_clock_phase("0.0000034901029295", "0.0000034901029346",
                                        after.source_time)
        self.assertGreater(theta_after.lower, theta_before.upper)

    def test_protocol_has_external_ramps_and_actual_retained_timing(self):
        protocol = self.protocol()
        self.assertEqual([s.ledger_matching for s in protocol.intervals],
                         [False, True, True, True, False])
        final = protocol.events[-1]
        self.assertTrue(final.source_time.contains(F("4.3371117917520605715")))
        self.assertLess(final.beta.lower, F("-7.841399681709530363"))
        self.assertGreater(final.beta.upper, F("-7.841369477578352354"))
        self.assertGreater(protocol.intervals[1].reference_energy.lower, 0)
        self.assertLess(protocol.intervals[2].reference_energy.upper, 0)

    def test_switch_work_telescopes_without_erasing_gross_exchange(self):
        protocol = self.protocol()
        self.assertEqual(len(protocol.work_pieces), 9)
        self.assertEqual(protocol.net_signed_work, 0)
        for column in range(4):
            self.assertEqual(sum(p.coefficients[column] for p in protocol.work_pieces), 0)
        self.assertEqual(protocol.positive_work, protocol.withdrawn_work)
        self.assertTrue(protocol.positive_work.contains(F("20.590661439892877")))
        self.assertGreater(protocol.positive_work.lower, 20)

    def test_shared_pi_cancels_after_reverse(self):
        args = (Interval.point(1), Interval.point(F(1, 5)), Interval(3, F(7, 2)),
                Interval.point(11), Interval.point(9))
        # The intentionally broad enclosure still cancels exactly at reversal.
        args = args[:2]+(Interval(F(31, 10), F(7, 2)),)+args[3:]
        protocol = paid_reference_protocol(*args)
        self.assertEqual(protocol.events[3].beta, Interval.point(F(-71, 100)))

    def test_unwrap_requires_prefixes_and_recovers_negative_turn(self):
        trajectory = [-i*0.1 for i in range(81)]
        principal = [math.remainder(x, 2*math.pi) for x in trajectory]
        lifted = unwrap_reference_phase(principal, maximum_step=0.11)
        self.assertAlmostEqual(lifted[-1], -8.0)
        self.assertNotAlmostEqual(principal[-1], lifted[-1])
        with self.assertRaises(ValueError):
            unwrap_reference_phase([0, 2], maximum_step=0.5)
        with self.assertRaises(ValueError):
            unwrap_reference_phase([0], maximum_step=math.pi)

    def test_invalid_source_enclosures_fail(self):
        for energy in (Interval(-1, 1), Interval(9, 11)):
            with self.assertRaises(ValueError):
                paid_reference_protocol(energy, 1, Interval("3.14", "3.15"), 11, 9)
        with self.assertRaises(ValueError):
            paid_reference_protocol(1, 0, Interval("3.14", "3.15"), 11, 9)


class CorrelatedClockPhase(unittest.TestCase):
    def test_every_positive_lift_has_negative_correlated_change(self):
        for a in (F(1, 10**12), F(1, 100), F(9, 10)):
            enclosure = correlated_phase_bounds(2, 3, a, 5)
            exact_low = -3*(1-math.sqrt(1-float(a)))*5
            exact_high = -2*(1-math.sqrt(1-float(a)))*5
            self.assertLess(enclosure.upper, 0)
            # Tiny a: evaluate the root difference without cancellation.
            delta = float(a)/(1+math.sqrt(1-float(a)))
            self.assertLessEqual(float(enclosure.lower), -3*delta*5+1e-15)
            self.assertGreaterEqual(float(enclosure.upper), -2*delta*5-1e-15)
            if a > F(1, 10**6):
                self.assertLessEqual(float(enclosure.lower), exact_low+1e-14)
                self.assertGreaterEqual(float(enclosure.upper), exact_high-1e-14)

    def test_correlated_sign_is_not_independent_band_resolution(self):
        threshold = independent_band_threshold(999, 1000)
        a = threshold/100
        self.assertLess(a, threshold)
        self.assertLess(correlated_phase_bounds(999, 1000, a, 1).upper, 0)
        self.assertEqual(correlated_phase_bounds(1, 2, 0, 10), Interval.point(0))
        self.assertEqual(correlated_phase_bounds(1, 2, F(1, 10), 0), Interval.point(0))

    def test_rational_root_margins_and_invalid_physical_chart(self):
        a = F(17, 100)
        n_lower = 2*(1-a)/(2-a)
        n_upper = 1-a/2
        self.assertEqual(1-a-n_lower*n_lower, a*a*(1-a)/(2-a)**2)
        self.assertEqual(n_upper*n_upper-(1-a), a*a/4)
        for args in ((0, 2, F(1, 10), 1), (2, 1, F(1, 10), 1),
                     (1, 2, 1, 1), (1, 2, F(1, 10), -1)):
            with self.assertRaises(ValueError):
                correlated_phase_bounds(*args)


if __name__ == "__main__":
    unittest.main()
