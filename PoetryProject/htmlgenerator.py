# TODO: 
# - [ ] create a postgres container
# - [ ] connect to the database
# - [ ] create table and insert dummy data using psql
# - [ ] read using python from db and generate pdf


from domonic import *

invoice_number = "INV001"
date = "2023-11-09"
customer_name = "John Doe"
total_amount = "$100.00"
invoice_lines = [
    {"description": "Energy", "quantity": 1, "unit_price": "$50.00", "total": "$50.00"},
    {"description": "Gas", "quantity": 2, "unit_price": "$25.00", "total": "$50.00"},
]

def generate_invoice_template(invoice_number, date, customer_name, total_amount, invoice_lines):

    # HTML template
    template = html(
        head(
            
            style(),
            script(),
        ),
        body(
            div(
                div(
                    "Invoice " + invoice_number,
                    _class="header",
                    _style="text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 20px;",
                ),
                div(
                    p("Date: " + date),
                    p("Customer: " + customer_name),
                    _class="details",
                    _style="margin-bottom: 20px;",
                ),
                table(
                    thead(
                        tr(
                            th("Description"),
                            th("Quantity"),
                            th("Unit Price"),
                            th("Total"),
                        )
                    ),
                    tbody(
                        *[tr(td(item["description"]), td(item["quantity"]), td(item["unit_price"]), td(item["total"])) for item in invoice_lines],
                        _class="items-table",
                        _style="width: 100%; border-collapse: collapse; margin-bottom: 20px;",
                    ),
                ),
                div("Total Amount: " + total_amount, _class="total", _style="font-size: 18px; font-weight: bold; text-align: right;"),
                _class="invoice",
                _style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #ccc; font-family: 'Arial', sans-serif;",
            ),
        )
    )

    # Output HTML
    output = render(template)

    # Save to a file
    with open('invoice_template_domonic.html', 'w') as file:
        file.write(output)

if __name__ == "__main__":
    generate_invoice_template(invoice_number, date, customer_name, total_amount, invoice_lines)


