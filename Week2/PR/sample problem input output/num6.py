#input
desired_grade = input("Enter desired grade> ")
minimum_average_required = float(input("Enter minimum average required> "))
current_average = float(input("Enter current average in course> "))
final_exam_percentage = float(input("Enter how much the final counts as a percentage of the course grade> "))

#rumus untuk menghitung final score needed
needed_final_score = (minimum_average_required - (current_average * (1 - final_exam_percentage / 100))) / (final_exam_percentage / 100)
 
#output
print(f"Anda membutuhkan skor {needed_final_score:.2f} pada ujian akhir untuk mendapatkan nilai {desired_grade}.")
