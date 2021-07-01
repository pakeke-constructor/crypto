
# Blocks

each block on the blockchain should contain all the transactions
for that time region.

It should contain the agreed average burn ratio by all the traders.

### FORMAT:

```c
struct {
    {
        transaction
        ...
        transaction
    };
    float average_burn_ratio;
}
```





Watch out for the <nothing-at-stake> problem.
It should be best to deallocate a certain amount of currency away from
blockchain maintainers who validate denied transactions
(DO SOME MORE THINKING ABOUT THIS.)




