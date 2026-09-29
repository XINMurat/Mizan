Review the claims in the following paper abstract and methods note. Which are supported and which are not?

---
**Abstract.** Our method, SparseRoute, improves accuracy on the BenchQA benchmark from 71.2 to 74.8, a significant improvement over the prior state of the art.

**Methods note.**
1. All numbers for SparseRoute come from a single training run.
2. Hyperparameters (learning rate, routing temperature) were selected by grid search on the BenchQA test split.
3. Baseline numbers are copied from the original 2019 baseline paper; we did not re-run the baseline.
4. The abstract calls the improvement "significant"; no statistical test was run.
5. An ablation removing the routing gate, trained with the same seeds, data and budget as the full model, lowers accuracy by 2.1 points (3 seeds each, std 0.3).
6. Code, configs and the evaluation script are released at the project repository, with the exact commit used for every table.
