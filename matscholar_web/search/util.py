import copy

from dash.dependencies import Input, Output, State

from matscholar_web.constants import valid_entity_filters


def get_entity_boxes_callback_args(as_type="state"):
    """
    Return all available entity boxes as Inputs, Outputs, or States.

    Args:
        as_type (str): "state" for State, "input" for Input, or "output" for
            Output

    Returns:
        (list): The list of inputs, states, or outputs plotly dash dependency
            objects on the search page.
    """
    type_dict = {
        "state": State,
        "output": Output,
        "input": Input
    }
    t = type_dict[as_type]
    return [t(f + '_filters_input', 'value') for f in valid_entity_filters]


def parse_search_box(search_text):
    """
    Parse the entity search text box

    Args:
        search_text (Str): The text in the search box, e.g.
            "material: PbTe, property: thermoelectric"

    Returns:
        entity_query (dict): The entities from the search text in dict format,
            e.g., {"material": "PbTe", "property": "thermoelectric"}

    Returns:

    """
    entities_text_list = search_text.split(",")
    entity_query = {k: [] for k in valid_entity_filters}
    for et in entities_text_list:
        for k in valid_entity_filters:
            entity_type_key = f"{k}:"
            if entity_type_key in et:
                query_entity_term = copy.deepcopy(et)
                query_entity_term = query_entity_term.replace(entity_type_key,
                                                              "").strip()
                entity_query[k].append(query_entity_term)
    entity_query = {k: v for k, v in entity_query.items() if v}
    return entity_query