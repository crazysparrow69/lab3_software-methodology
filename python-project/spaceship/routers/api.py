from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def matrix() -> dict:
    matrix_a = np.random.rand(10, 10)
    matrix_b = np.random.rand(10, 10)

    product = np.dot(matrix_a, matrix_b)

    result = {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": product.tolist()
    }

    return result
