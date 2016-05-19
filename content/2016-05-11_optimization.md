title: Optimization and dimensionality reduction
data: 2016-05-11
category: notes
tags: lasso regression, notes, active-set, dimensionality reduction

The results of Lasso regression have shown that the time complexity is quite large and cannot be feasible for larger k. In this paragraph, I will address some scalable techniques to reduce the time complexity by using typically two approaches: optimization and dimensionality reduction.

## Optimization algorithm

#### Active-set

By observing that the selected number of features is immensely smaller than the total number, one could be using a classic optimization method: active-set. Since the main idea of active-set is activating the constraints gradually, it can easily be combined with another optimization algorithm, e.g. FISTA in our case. This method is detailed in the [book][1].

#### Optimization algorithm

For the moment, the optimization algorithm for Lasso is FISTA, but we could find faster algorithm in the future.

## Dimensionality reduction

Another approach to reduce the time complexity is to reduce the dimension of the feature matrix before using Lasso regression. Concretely, the problem can be described as follows: given a n-by-p matrix, how to find an approximated n-by-q matrix with q smaller than p?

Dimensionality reduction leads to lower time complexity, but in the contrast, it could cause lower accuracy. The generic methods consists of matrix factorization, feature selection and feature hashing.

#### Matrix factorization

As I mentioned in last blog, the majority of matrix factorization methods don't work in our case, as they don't preserve the sparsity of matrix. The only interesting factorization in our case is **CUR decomposition**. However, this approach is usually very expensive in terms of time complexity.

#### Feature selection

Feature selection attempts to remove redundant or irrelevant features based on some scoring functions (e.g. by comparing the tf-idf of each feature) in order to improve the prediction performance and efficiency of learning algorithms. This approach is usually very fast but can result in some loss of information.

#### Feature hashing

Another approach is related to hashing tricks. It is designed to map very high dimensional input spaces into lower dimensional spaces. An arbitrary hash function was used to classify protein sequence ([Protein Sequence Classification Using Feature Hashing][2]), but this arbitrary choice of hash function could lead to unexpected result and doesn't exploit the inner relation in the data. A typical hashing, which tends to map similar items into the same 'buckets', is [LSH][3]. LSH has much in common with data clustering and feature abstraction. In fact, LSH serves as a merging tool to create abstract features, which can be seen as a [*regularizer*][4]. Furthermore, the efficiency of the LSH leads to very fast approximate [hierarchical clustering algorithm][5]. Thus, I propose here the following scheme for hashing and merging features (feature agglomeration):

1. hierarchical clustering on features
2. merging the features in the same cluster by taking the union of these features
3. return feature matrix with reduced dimension

## Experiments

#### Active-set
The algorithm of active-set can be separated into two parts: a function terminate to indicate if the program ends, and the main function active_set_run.

```
terminate(X, residual, lamb, active_set, stepsize, tol):
  w = max(|X.T.dot(residual)|)
  if w <= lamb*(1+tol):
    return True
  else:
    update(active_set) # update active_set by adding stepsize more features
    return False
```

```
active_set_run(Y, X, max_num_selected, stepsize, **param):
  residual = Y
  w0 = zeros((stepsize,1))
  while len(active_set) < max_num_selected and not terminate(X, residual, lamb, active_set, incr):
    w0 = [w0, zeros((stepsize,1))]
    w0 = optimization_algo(Y, X, w0, **param)
  w = zeros((X.shape[1],1))
  w[active_set] = w0
  return w
```

In our algorithm, I have tested active-set by adding 100 features violating the criteria for k-mers of lengths smaller than 10, and have found the running time is 2-times faster than initial algorithm. I observed that the cost time of optimization is far bigger than that of the termination checking process.

#### LSH and hierarchical clustering

Notice that active-set allows to select features incrementally, It seems that compression techniques would not improve a lot on optimization speed since only a small subset of features is worked on.

I have carried a [single linkage clustering][6] using LSH on the feature matrix of length k <= 10. The number of the features after compression becomes 144488 (before 212164). The number of selected features is almost equal to that before hashing, and the cost time of optimization is lower. But if we take account of the time spent on the clustering and hashing step, the total running time is almost equal.


[1]: http://lear.inrialpes.fr/people/mairal/resources/pdf/ftml.pdf
[2]: http://www.cse.unt.edu/~ccaragea/papers/bibm11.pdf
[3]: https://en.wikipedia.org/wiki/Locality-sensitive_hashing
[4]: http://web.cs.iastate.edu/~honavar/Papers/adrian-icdm09.pdf
[5]: http://link.springer.com/article/10.1007%2Fs10115-006-0027-5
[6]: https://en.wikipedia.org/wiki/Single-linkage_clustering
