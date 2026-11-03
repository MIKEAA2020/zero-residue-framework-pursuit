# Tier-0 Global-Mode Null v1
## Declared common-mode stress test for blind candidate discovery

## Purpose

The initial blind pipeline rejects a simple direct-bypass null. That is necessary but insufficient: shared global structure can make local regions look integrated or mutually predictive without supporting independent bounded candidates. This extension adds a declared global mode while keeping the blind pipeline’s one-node boundary budget and thresholds unchanged.

---

## Construction

Start with the two-controller M2-v2 system and add a global binary state \(g_t\). It evolves as
\[
\Pr(g_{t+1}=1\mid X_t)=s(-0.2+0.8g_t).
\]
Add a direct \(g_t\to m_{a,t+1}\) and \(g_t\to m_{b,t+1}\) coefficient of \(1.0\). The two apparent local modules therefore share a global driver in addition to their local interface/exterior chain.

The process is not intended as a realistic common-cause model. It is a transparent stress test: global coupling must be visibly represented in the supplied graph rather than silently hidden.

---

## Expected blind outcome

For a candidate interior \(A=(y_1,y_2,m)\), the usual local boundary \(B=b\) no longer separates \(A\) from its exterior because \(g\in R\) directly enters \(m\). Choosing \(B=g\) instead leaves the local \(b\)-to-\(m\) route unblocked. Under the frozen one-node boundary budget, there is no admissible local candidate with full graph separation.

**Expected output: zero local candidates.**

This does not show that every global common-mode case is invalid. It shows that the v1 budget properly refuses to call two locally bounded candidates when their screening requires a larger/global interface than the budget permits.

---

## Limit and next extension

Because \(g\) is declared and graph-visible, this is a structural null, not a hidden-confounder test. A later v2 pipeline must allow multi-node interfaces with a complexity penalty and test whether conditioning on a declared global variable restores genuine local candidates without allowing the boundary to absorb arbitrary causal paths. Hidden global modes require graph-discovery and causal-identification work beyond this null.
