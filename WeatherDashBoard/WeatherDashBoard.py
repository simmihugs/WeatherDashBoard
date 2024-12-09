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


def my_form():
    return rx.form(
        rx.vstack(
            rx.input(placeholder="User Name", name="name", required=True),
            rx.input(placeholder="user@reflex.dev", name="email"),
            rx.select(
                ["Male", "Female"],
                placeholder="Female",
                name="gender",
            ),
            rx.button("Submit", type="submit"),
        ),
        on_submit=People.add_person,
        reset_on_submit=True,
    )


def index() -> rx.Component:
    return rx.vstack(
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
        my_form(),
    )


app = rx.App()
app.add_page(index)
