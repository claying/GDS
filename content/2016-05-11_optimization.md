title: Optimization and dimensionality reduction
data: 2016-05-11
category: notes
tags: lasso regression, notes, active-set, dimensionality reduction

The results of Lasso regression have shown that the time complexity is quite large and cannot be feasible for larger k. In this paragraph, I will address some scalable techniques to reduce the time complexity by using typically two approaches: optimization and dimensionality reduction.

## Optimization algorithm

#### Active-set

By observing that the selected number of features is immensely smaller than the total number, one could be using a classic optimization method: active-set. Since the main idea of active-set is activating the constraints gradually, it can easily be combined with another optimization algorithm, e.g. FISTA in our case. This method is detailed in the [book][1].

In our algorithm, I have tested active-set by adding 100 features violating the criteria for k-mers of lengths smaller than 10, and have found the running time is 2-times faster than initial algorithm.

#### Optimization algorithm

For instant, the optimization algorithm for Lasso is FISTA, but we could find faster algorithm in the future.

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


[1]: http://lear.inrialpes.fr/people/mairal/resources/pdf/ftml.pdf
[2]: http://www.cse.unt.edu/~ccaragea/papers/bibm11.pdf
[3]: https://en.wikipedia.org/wiki/Locality-sensitive_hashing
[4]: http://web.cs.iastate.edu/~honavar/Papers/adrian-icdm09.pdf
[5]: http://link.springer.com/article/10.1007%2Fs10115-006-0027-5
