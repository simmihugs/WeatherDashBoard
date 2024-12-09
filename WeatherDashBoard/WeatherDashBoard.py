"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    email: str
    gender: str


class People(rx.State):
    people: list[Person] = [
        Person("Simon", "simon.peter@post.mail", "cool"),
        Person("Zahra Ambessa", "zahra@example.com", "Female"),
        Person("Danilo Sousa", "danilo@example.com", "Male"),
    ]

    def add_person(self, form_data: dict):
        self.people.append(Person(**form_data))


def to_row(person: Person):
    return rx.table.row(
        rx.table.column_header_cell(f"{person.name}"),
        rx.table.column_header_cell(f"{person.email}"),
        rx.table.column_header_cell(f"{person.gender}"),
    )


def form():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26), rx.text("Add User", size="4")),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Add New User",
            ),
            rx.dialog.description(
                "Fill the form with the user's info",
            ),
            rx.form(
                rx.flex(
                    rx.input(placeholder="User Name", name="name", required=True),
                    rx.input(placeholder="user@reflex.dev", name="email"),
                    rx.select(
                        ["Male", "Female"],
                        placeholder="Female",
                        name="gender",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="grass"),
                        ),
                        rx.dialog.close(
                            rx.button("Submit", type="submit"),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=People.add_person,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )


def index() -> rx.Component:
    return rx.vstack(
        form(),
        rx.table.root(
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
            variant="surface",
            size="3",
        ),
    )


app = rx.App()
app.add_page(index)
