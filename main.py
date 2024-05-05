from Recommendation import get_recommendation
from StudyPattern import genetic_algorithm
from PDFtopython import extract_uni_timetable
from TimetableLogic import merge_timetables
from WeeklyTimetable import update_timetable_manually

def main():
    recommendation_dict = get_recommendation()

    # Run genetic algorithm
    best_individual = genetic_algorithm(100, 50, 0.1, recommendation_dict)
    print("Recommended study pattern:")
    print(best_individual)
    
    #Extract the university timetable from PDF
    pdf_path = "Timetable - 8th Sem.pdf"
    uni_timetable = extract_uni_timetable(pdf_path)
    
    #Generate the timetable
    generated_timetable = merge_timetables(best_individual, uni_timetable)
    
    #Update the timetable manually
    update_timetable_manually(generated_timetable)
   
        
    
if __name__ == "__main__":
    main()

