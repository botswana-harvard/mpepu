from bhp_model_describer.views import base_model_group_describer


def model_group_describer(request, **kwargs):
    
    app_list = ['mpepu_maternal', 'mpepu_infant']

    return base_model_group_describer(request, app_list=app_list, **kwargs)
