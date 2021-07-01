
## PROOF OF WORK CRYPTOCURRENCY

Heres how I understand it:


Each node on the network keeps a digital record of all transactions (compressed, of course)

"Miners" are nodes on the network who control the majority of processing power,
and are the "regulators" of the bitcoin protocol.

Miners are encouraged to keep the bitcoin protocol secure by being paid in bitcoin.
If miners *somehow* colluded to screw people over, the value of bitcoin would drop, and miners would get paid less.



Lets say Alice sends 5 btc to Bob:
   Alice emits a call to some miners she knows:   "transaction:   Alice -> Bob, 5",
   including her <private_key> signature to prove that it is her.

   A few miners around the world pick up on the transaction call, and those miners adds that
       transaction to their personal ledger if its valid.    (i.e. if Alice has enough money.) 

   The miner then sends that transaction to the rest of the network. <see_NB_1.>


<NB_1>:  {
What incentives do miners have to send random people's transactions to other nodes?
Transactions contain tips.
If the miners happen to validate the block containing the transaction, they
will get a small tip from the person sending the transaction.

If they *dont* send the transaction to other miners, the transaction may not be recognized as legit,
and the miner will have validated a block that is not recognized as legit by the majority of the nodes.

In short, the computational cost to spread the news of a transaction is WAYYY LESS than the computational
cost of validating a block that is invalid. Thus, it is in the miner's interest to spread news of new transactions.
}





