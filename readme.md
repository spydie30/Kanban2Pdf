
# Kanban Board PDF Generator

This project provides a utility to generate a well-formatted PDF report from a Trello board JSON data. The PDF includes details about lists and cards, such as card titles, descriptions, labels, and member names.

## Features

- **Load Trello Board Data**: Read JSON data for a trello board from a file.
- **Format and Generate PDF**: Create a PDF report that includes:
  - Kanban board name
  - List titles and descriptions
  - Card details including titles, descriptions, labels, and members
- **User Input**: Allows users to select which lists to include in the PDF report.

## Requirements

- Python 3.x
- `reportlab` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/kanban-pdf-generator.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd kanban-pdf-generator
   ```

3. **Install dependencies**:
   ```bash
   pip install reportlab
   ```

## Usage

1. **Prepare Your Kanban Board JSON File**: Ensure you have a JSON file that includes the structure for `lists`, `cards`, `labels`, and `members`.

2. **Run the Script**:
   ```bash
   python kanban_pdf_generator.py
   ```

   - The script will prompt you to enter the names of the lists you want to include in the PDF. 
   - The PDF will be generated with the name `kanban_report.pdf` in the current directory.

## JSON Structure

The JSON file should have the following main keys:

- `id`
- `name`
- `desc`
- `lists`: A list of lists with `id`, `name`, and `desc`.
- `cards`: A list of cards with `id`, `name`, `desc`, `idList`, `idLabels`, and `idMembers`.
- `labels`: A list of labels with `id`, `name`, and `color`.
- `members`: A list of members with `id` and `fullName`.

### Example JSON

```json
{
  "id": "658da386b376fa21c53f13b2",
  "name": "Gallard Steels ERP",
  "desc": "",
  "lists": [
    {
      "id": "658da407da857c99a17975e3",
      "name": "Rough notes",
      "desc": ""
    }
  ],
  "cards": [
    {
      "id": "66309687c8ede43bf71af8df",
      "name": "Trello Guidelines",
      "desc": "Use this template to log …",
      "idList": "658da407da857c99a17975e3",
      "idLabels": ["658da389821d4948f2578657"],
      "idMembers": ["654b9d690ff0b85715bb34a7"]
    }
  ],
  "labels": [
    {
      "id": "658da389821d4948f2578657",
      "name": "Notes",
      "color": "blue"
    }
  ],
  "members": [
    {
      "id": "654b9d690ff0b85715bb34a7",
      "fullName": "John Doe"
    }
  ]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
