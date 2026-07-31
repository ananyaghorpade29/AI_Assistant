import faiss
import numpy as np

vectors = np.array(
    [
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
    ],
    dtype="float32",
)

dimension = 2

index= faiss.IndexFlatL2(dimension)
index.add(vectors)

query = np.array(
	[[1.0,0.2]],
	dtype="float32",
	)

distances, indices = index.search(query,k=1)

print("Distance: ")
print(distances)

print("\nIndices: ")
print(indices)
