# Luma NLP Engineering Interview


## Details 
1.  Dataset location: https://storage.googleapis.com/kaggle-data-sets/176267/397518/compressed/yelp_academic_dataset_review.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201003%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201003T211134Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=79eb5d144ea2ac989674de896da865696febc2e8fcd796cf19413142ffd88effd3bfe2320e823ec162ff8c842f48e2424fb24b7ded445f2e44dd6e1aa1056992d155fc4ddd90026e972b75479b1df773ef0fe163f73636a9eaa2cf56c9c4bfc8d279dc851509a6a3d538ae40497d0392edf5680969ea6a8214c6db040a9c061b81dad779992199083d32e59484b95c0a12cdda39360804a4955b2a61614ba4a5fdd013c023ec1e979bd22ec1c89faf900754f6cd76146e2f771f79931895f9d87b857e97a1419f28833d00880a5a643d11c95dceb7009b6c6a8b4e6873392a1a0517772d5b79e6640e9dc1768635c3efd0276a27f40c6024574ce3a97307b583

2. Embeddings can be found in https://www.kaggle.com/gmhost/gru-capsule

2. 1 and 2 stars are negative. 3 stars are neutral. 4 and 5 stars are positive.

3. Model explanation is in the 'Model Design.ipynb'

4. There are two files required for the API to run, they can be found in https://gofile.io/d/qSpSil


## To run in linux os

1. Create python env
2. pip install -r requirements.txt
3. python server.py   -----  /docs for easy swagger


