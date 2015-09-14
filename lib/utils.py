from flask import jsonify

# Helper functions

def api_error(reason, status_code=400):
    json = jsonify({'error': reason})
    json.status_code = status_code
    return json

def check_params_exist(request, params):
    if request.method == 'POST':
        for param in params:
            if request.form[param] is None:
                return False
        return True

    if request.method == 'GET':
            for param in params:
                if request.args.get(param) is None:
                    return False
            return True
