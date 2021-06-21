

# MALBR Mechanism
```
Market-cap activated linear burn ratio: (MALBR)

A coefficient that adds burn rate when the market cap is low.
(Market cap is with respect to the highest market cap currency at the time.)
For example,  let   BR(M) be the burn ratio of the crypto, where M is the market cap,
and K is the target market cap:

BR(M) = max(0, 1 - (M / K)) / 2 
```


This provides a linear burn ratio from market cap 0 -> K.
When market cap is >= K, no burn is applied.
When market cap is 0, 50% burn is applied
The question is, how would we implement this. 
By nature, market data is centralized. We need a good way to decentralize it.
Without a good system, POS nodes could be incentivized to lie about the market cap ratio when trading, as they could get a higher cut. 


We could get around this by implementing a linear penalty when sending currency and getting a market cap that is far different to other nodes on the network.
If the market cap is determined by the weighted average of nodes who own the majority of the coin, then nodes can be incentivized to tell the truth. 


**PROPOSAL:**
Let the weighted average burn ratio be `Ab`, 
Let a node's stated burn ratio be `Gb`.  (clamped from 0-1 to prevent tampering obviously) 
Let `BR` be the function from before.
The burn rate for individual nodes can then be given by:
```lua
BI = BR(Ab) + |Gb - Ab|
```
Thus, the more wrong a node is in their stated market cap, the more burn penalty they are likely to recieve.
Therefore, it is in a rational node's best interest to abide to the protocol to minimize the chance of them having extra coins burned.

Obviously, in this regard, if many rich nodes colluded and agreed that the market cap of the coin was super high at all times, then there would be no burn, and honest nodes would be penalized.  (51% attack-esque.)
However, we are assuming that this kind of collusion is not feasibly possible; at least, not at a scale that would cause noticeable damage, as rational POS nodes are incentivized to keep the integrity of the coin stable.




