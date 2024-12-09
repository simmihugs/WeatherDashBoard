"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


class People(rx.State):
    people: list[tuple[str]] = [
        ("Simon", "simon.peter@post.mail", "cool"),
        ("Zahra Ambessa", "zahra@example.com", "Female"),
        ("Danilo Sousa", "danilo@example.com", "Male"),
    ]


def to_row(person: tuple[str]):
    return rx.table.row(
        rx.table.column_header_cell(f"{person[0]}"),
        rx.table.column_header_cell(f"{person[1]}"),
        rx.table.column_header_cell(f"{person[2]}"),
    )


def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(People.people, to_row),
        ),
    )


app = rx.App()
app.add_page(index)
