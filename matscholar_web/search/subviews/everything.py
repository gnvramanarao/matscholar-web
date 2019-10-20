import dash_html_components as html

from matscholar_web.search.subviews.abstracts import abstracts_results_html
from matscholar_web.search.subviews.entities import entities_results_html
from matscholar_web.search.subviews.materials import materials_results_html
from matscholar_web.search.util import no_results_html


def everything_results_html(entity_query, raw_text):

    scroll_down_header_txt = "Scroll down for full results."
    scroll_down_header = html.Div(scroll_down_header_txt, className="is-size-3")
    scroll_down = html.Div(
        [
            scroll_down_header,
        ],
        className="notification is-light has-text-centered"
    )
    scroll_down_column = html.Div(scroll_down, className="column is-half")
    scroll_down_columns = html.Div(scroll_down_column, className="columns is-centered")
    scroll_down_container = html.Div(scroll_down_columns, className="container")

    entities_results = entities_results_html(entity_query, raw_text)
    materials_results = materials_results_html(entity_query, raw_text)
    abstracts_results = abstracts_results_html(entity_query, raw_text)
    all_results = [entities_results, materials_results, abstracts_results]
    no_results = no_results_html()

    if all([str(r) == str(no_results) for r in all_results]):
        return no_results
    else:
        container = html.Div(
            [
                scroll_down_container,
                entities_results,
                materials_results,
                abstracts_results,
            ],
            className="container"
        )
        return container