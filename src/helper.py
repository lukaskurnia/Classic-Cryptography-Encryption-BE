from src.algorithm.playfair import Playfair

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
    algo_switcher = {
        "playfair": Playfair(text, key) 
    }

    algo_invalid = "algorithm invalid"
    obj = algo_switcher.get(algorithm, algo_invalid)
    if (obj == algo_invalid):
        raise Exception(algo_invalid, 400) 

    mode_switcher = {
        "encrypt": obj.encrypt(),
        "decrypt": obj.decrypt()
    }

    mode_invalid = "mode invalid"
    chipper_text = mode_switcher.get(mode, mode_invalid)
    if (chipper_text == mode_invalid):
        raise Exception(mode_invalid, 400) 

    return chipper_text