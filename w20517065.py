# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
 
# Any code taken from other sources is referenced within my code solution.

##rstrip
## https://stackoverflow.com/questions/25352090/python-program-prints-an-extra-empty-line-when-reading-a-text-file
##colors:
##https://matplotlib.org/stable/gallery/color/named_colors.html
##
##global keyword:
##https://www.w3schools.com/python/python_variables_global.asp
##
##max count
##https://stackoverflow.com/questions/3090175/find-the-greatest-largest-maximum-number-in-a-list-of-numbers
##


# Student ID: 20230486 / w20517065
# Date: 27/11/2023




from graphics import *  

# student count for each category
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
total_count = 0

# histogram data
chart_height = 600
bar_width = 80
bar_gap = 20
initial_gap = 40
footer_gap = 100
bar_height_multiplier = 1

# Initialize a list to store progression data
progression_data = []


# Function to save progression data to the list
def save_progression_data(outcome, pass_credits, defer_credits, fail_credits):
    progression_data.append([outcome, pass_credits, defer_credits, fail_credits])


# get user input for credit types
def get_credits(question):
    while True: # repeat until the input is correct
        try:
            credits = int(input(question))
            if credits not in range(0, 121, 20): 
                print("Out of range")
            else:
                return credits
        except ValueError: # when non integer valud is entered
            print("Integer required")

# print result and update counts
def show_result(pass_credits, defer_credits, fail_credits):
    # need to use global keyword to update global variables
    global total_count
    global progress_count
    global trailer_count
    global retriever_count
    global excluded_count
    
    
    if pass_credits == 120:
        save_progression_data("Progress", pass_credits, defer_credits, fail_credits)
        print('Progress')
        progress_count += 1
    elif pass_credits >= 100:
        save_progression_data("Progress (module trailer)", pass_credits, defer_credits, fail_credits)
        print('Progress(module trailer)')
        trailer_count += 1
    elif fail_credits >= 80:
        save_progression_data("Exclude", pass_credits, defer_credits, fail_credits)
        print('Exclude')
        excluded_count += 1
    else:
        progression_data.append(["Module retriever", pass_credits, defer_credits, fail_credits])
        print('Module retriever')
        retriever_count += 1 

   

def calculate_total_count():
    return progress_count + trailer_count + retriever_count + excluded_count

# Function to display the stored data in the specified format
def display_progression_data():
    for data in progression_data:
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")


def write_progression_data(file_name):
    f = open(file_name , 'w')
    for data in progression_data:
        f.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
    f.close()

def read_progression_data(file_name):
    f = open(file_name, "r")
    for line in f:
      print(line.rstrip('\n')) #using rstrip to avoid printing extra line

# calculate bar_height_multiplier depending on the highest count(highest bar). Otherwise the bars will appear small
def calculate_bar_height_multiplier():
    highest_count = max(progress_count, trailer_count, retriever_count, excluded_count)

    if highest_count == 0:
        multiplier = 1
    else:
        multiplier = (chart_height - 200)/highest_count #200 is the estimated space for header and footer
    
    return multiplier

    
def show_histogram():
    global bar_height_multiplier
    bar_height_multiplier = calculate_bar_height_multiplier()

    ## create window
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("Mint Cream")

    draw_histogram_header(win)
    
    draw_histogram_bar(win, 0, "Progress", progress_count, "greenyellow")
    draw_histogram_bar(win, 1, "Trailer", trailer_count, "lightgreen")
    draw_histogram_bar(win, 2, "Retriever", retriever_count, "darkseagreen")
    draw_histogram_bar(win, 3, "Excluded", excluded_count, "pink")

    draw_histogram_footer(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done
    
# histogram header information
def draw_histogram_header(win):
    heading = Text(Point(200, 30), 'Histogram Results')
    heading.draw(win)
    heading.setTextColor("grey")
    heading.setSize(24)
    heading.setStyle("bold")
    heading.setFace("helvetica")

# histogram footer information
def draw_histogram_footer(win):
    footer = Text(Point(150, win.getHeight() - footer_gap + 50), str(calculate_total_count()) + " outcomes total")
    footer.draw(win)                                    
    footer.setTextColor("grey")
    footer.setSize(20)
    footer.setFace("helvetica")

    base_line = Rectangle(Point(20, win.getHeight() - footer_gap), Point((bar_width + bar_gap)*4 + 40, win.getHeight() - footer_gap))
    base_line.draw(win)

# draw a histogram bar
def draw_histogram_bar(win, bar_index, bar_name, count, color):
    # calculate bar x cordinates depending on parameters
    bar_x = initial_gap + bar_index * (bar_width + bar_gap)
    bar_height = bar_height_multiplier*count # multiply by bar_height_multiplier to inclrese visual height, otherwise bar will be too short

    #create bar rectangle
    rectangle = Rectangle(Point(bar_x, win.getHeight() - footer_gap), Point(bar_x + bar_width, win.getHeight() - footer_gap - bar_height))
    rectangle.setFill(color)
    rectangle.draw(win)

    #bar count text
    count_text = Text(Point(bar_x + bar_width/2, win.getHeight() - footer_gap - bar_height - 20), str(count))
    count_text.draw(win)

    #bar_name_text
    bar_name = Text(Point(bar_x + bar_width/2, win.getHeight()- footer_gap + 20), bar_name)
    bar_name.draw(win)


def main():
    user_type = input("Are you a student or a staff member?"
                      "\n Enter 'student' or 'staff': ") 
    if user_type == 'student':
        pass_credits = get_credits("Enter your credits at pass:")
        defer_credits = get_credits("Enter your credits at defer:")
        fail_credits = get_credits("Enter your credits at fail:")

        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:
            print('Total incorrect')
        else:
            show_result(pass_credits, defer_credits, fail_credits)

    elif user_type == 'staff':
        while True:
            pass_credits = get_credits("Enter your credits at pass:")
            defer_credits = get_credits("Enter your credits at defer:")
            fail_credits = get_credits("Enter your credits at fail:")

            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits != 120:
                print('Total incorrect')
            else:
                show_result(pass_credits, defer_credits, fail_credits)

            another_set = input("Would you like to enter another set of data?"
                                "\n Enter 'y' for yes or 'q' to quit and view results: ")
            if another_set.lower() == 'q':
                break
        write_progression_data('progression_data.txt')
        total_count = calculate_total_count()
        show_histogram()

        # Part 2
        print("\nPart 2:")
        display_progression_data()

        # Part 3
        print("\nPart 3:")
        read_progression_data('progression_data.txt')

    else:
        print("Invalid role. Please enter 'student' or 'staff'.")

main()


