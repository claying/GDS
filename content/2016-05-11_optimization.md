title: Optimization and dimensionality reduction
data: 2016-05-11
category: notes
tags: lasso regression, notes, active-set, dimensionality reduction

The results of Lasso regression have shown that the time complexity is quite large and cannot be feasible for larger k. In this paragraph, I will address some scalable techniques to reduce the time complexity by using typically two approaches: optimization and dimensionality reduction.

## Optimization algorithm

By observing that the selected number of features is immensely smaller than the total number, one could be using a classic optimization method: active-set. Since the main idea of active-set is activating the constraints gradually, it can easily be combined with another optimization algorithm, e.g. FISTA in our case. This method is detailed in the [book][1].

In our algorithm, I have tested active-set by adding 100 features violating the criteria for k-mers of lengths smaller than 10, and have found the running time is 2-times faster than initial algorithm.

## Dimensionality reduction

Another approach to reduce the time complexity is to reduce the dimension of the feature matrix. Concretely the problem can be described as follows: given a n-by-p matrix, how to find an approximated n-by-q matrix with q smaller than p?

Dimensionality reduction leads to lower time complexity, but in the contrast, it could cause lower accuracy. The generic methods consists of matrix factorization and feature hashing. As I mentioned in last blog, the majority of matrix factorization methods don't work in our case, as they don't preserve the sparsity of matrix. The only interesting factorization in our case is **CUR decomposition**. However, this approach is usually very expensive in terms of time complexity. We thus can focus on another approach related to hashing tricks. An arbitrary hash function was used to classify protein sequence ([Protein Sequence Classification Using Feature Hashing][2]), but this arbitrary choice of hash function could lead to unexpected result and doesn't exploit the inner relation in the data. A typical hashing, which tends to map similar items into the same 'buckets', is [LSH][3]. LSH has much in common with data clustering and feature abstraction. In fact, LSH serves as a merging tool to create abstract features, which can be seen as a *regularizer*. Furthermore, the efficiency of the LSH leads to very fast approximate hierarchical clustering algorithm.


[1]: http://lear.inrialpes.fr/people/mairal/resources/pdf/ftml.pdf
[2]: http://www.cse.unt.edu/~ccaragea/papers/bibm11.pdf
[3]: https://en.wikipedia.org/wiki/Locality-sensitive_hashing
