from src.algorithm.playfair import Playfair
from src.algorithm.affine import Affine
from src.algorithm.hill import Hill

def request_processor(text, key, algorithm, mode, is_binary):
    try:
        chipper_text = algorithm_processor(text, key, algorithm, mode, is_binary)
        return chipper_text, 200

    except Exception as err:
        if (len(err.args) > 1):
            return err.args[0], err.args[1]
        else:
            # only uncomment below code for debugging purpose
            raise err
            
            return "internal server error", 500           

def algorithm_processor(text, key, algorithm, mode, is_binary):
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

    if is_binary:
        # TODO: lukas ubah ini jadi nama algorithmnya ntar 
        if algorithm != "test":
            raise Exception(f"binary file can't be {mode}ed with {algorithm}", 400) 

        obj.preprocess(is_binary)
    else:
        obj.preprocess()

    if mode == "encrypt":
        chipper_text = obj.encrypt()
    elif mode == "decrypt": 
        chipper_text = obj.decrypt()
    else:
        raise Exception("mode invalid", 400) 

    return chipper_text

def convert_file_to_string(data):
    file = data.read()
    decoded = file.decode('utf-8')
    return decoded.replace('\n', '')