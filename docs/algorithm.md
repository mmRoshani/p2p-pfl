# Algorithm 1 PANM: Personalized Adaptive Neighbor Matching

Now we present PANM by combining the algorithms mentioned above. In the first stage, client i (i ∈ [n]) communicates randomly in the network while conducting NSMC for T1 rounds. The neighbor list Nit in the last round of the first stage is set as the initial neighbor bag in the second stage, BT1+1 i = NT1 i . In the second stage, client i operates gossip communication with peers Nit (Nit j Bit, |Nit| = k) sampled from the neighbor bag for aggregation and performs NAEM every τ rounds to update the neighbor bag Bit. The process of PANM is shown in Algorithm 1.

---

<div style="text-align: center;">
  <img src="./assets/Algorithm 1 PANM: Personalized Adaptive neighbor Matching.png" alt="Algorithm 1 PANM: Personalized Adaptive neighbor Matching">
</div>

___
<div>
<div align="center">
  <img src="https://www.gnu.org/graphics/gplv3-127x51.png" width="85" title="hover text">
</div>
</div>
