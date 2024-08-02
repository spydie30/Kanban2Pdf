import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def load_kanban_board(file_path):
    with open(file_path, 'r') as file:
        kanban_board = json.load(file)
    return kanban_board

def generate_pdf(kanban_board, selected_lists):
    # Initialize PDF
    pdf_output_path = "kanban_report.pdf"
    doc = SimpleDocTemplate(pdf_output_path, pagesize=letter)
    story = []
    width, height = letter

    # Access lists and cards from the kanban board
    lists = kanban_board.get("lists", [])
    cards = kanban_board.get("cards", [])

    # Create a dictionary of cards organized by list ID
    cards_by_list = {}
    for card in cards:
        list_id = card.get("idList")
        if list_id:
            if list_id not in cards_by_list:
                cards_by_list[list_id] = []
            cards_by_list[list_id].append(card)

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    subtitle_style = styles['Heading2']
    text_style = styles['Normal']

    for list_ in lists:
        list_id = list_.get("id")
        list_name = list_.get("name", "No List Name")
        if list_name in selected_lists:
            # Add list title to PDF
            story.append(Paragraph(f'List: {list_name}', title_style))
            story.append(Spacer(1, 12))  # Spacer
            
            # Fetch cards associated with this list
            list_cards = cards_by_list.get(list_id, [])
            for card in list_cards:
                title = card.get("name", "No Title")
                description = card.get("desc", "No Description")

                # Add card details to PDF
                story.append(Paragraph(f'Card: {title}', subtitle_style))
                story.append(Paragraph(description, text_style))
                story.append(Spacer(1, 12))  # Spacer

    # Build the PDF
    doc.build(story)
    print(f"PDF generated: {pdf_output_path}")

def main():
    # Load the kanban board data
    kanban_board = load_kanban_board("./gsl_board.json")
    
    # Print all available list names to select from
    available_lists = [list_["name"] for list_ in kanban_board.get("lists", [])]
    print("Available Lists:")
    for list_name in available_lists:
        print(f"- {list_name}")
    
    # Ask the user to enter the list names to print, comma-separated
    selected_lists = input("Enter the lists to print (comma-separated): ").split(",")
    selected_lists = [name.strip() for name in selected_lists]  # Trim whitespace

    # Generate PDF or other processing for selected lists
    generate_pdf(kanban_board, selected_lists)

if __name__ == "__main__":
    main()
