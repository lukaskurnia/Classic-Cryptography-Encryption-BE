from src.algorithm.playfair import Playfair
from src.algorithm.affine import Affine
from src.algorithm.hill import Hill

def request_processor(text, key, algorithm, mode):
    try:
        chipper_text = algorithm_processor(text, key, algorithm, mode)
        return chipper_text, 200

    except Exception as err:
        if (len(err.args) > 1):
            return err.args[0], err.args[1]
        else:
            # only uncomment below code for debugging purpose
            raise err
            
            return "internal server error", 500           

def algorithm_processor(text, key, algorithm, mode):
    # Add new algorithm here
    algo_switcher = {
        "playfair": Playfair(text, key),
        "affine": Affine(text, key),
        "hill": Hill(text, key),
    }

    algo_invalid = "algorithm invalid"
    obj = algo_switcher.get(algorithm, algo_invalid)
    if (obj == algo_invalid):
        raise Exception(algo_invalid, 400) 

    obj.preprocess()
    
    if mode == "encrypt":
        chipper_text = obj.encrypt()
    elif mode == "decrypt": 
        chipper_text = obj.decrypt()
    else:
        raise Exception("mode invalid", 400) 

    return chipper_text