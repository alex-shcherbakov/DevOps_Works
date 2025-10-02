import os
from datetime import date

from DevOps_Sr2.model.AcademicPerformance import AcademicPerformanceImpl
from DevOps_Sr2.model.DesiredPerformance import DesiredPerformance
from DevOps_Sr2.model.Student import Student
from DevOps_Sr2.model.StudentData import StudentData
from DevOps_Sr2.savers.CSVSaver import CSVSaver
from DevOps_Sr2.savers.JSONSaver import JSONSaver
from DevOps_Sr2.savers.XMLSaver import XMLSaver


def main():

    print(" Запуск програми збереження даних про студента...")

    FULL_NAME = "Щербаков Олексій Олександрович"
    GROUP = "PDM-51"
    WORK_NUMBER = "SR2"

    # Дані для студентських класів
    subjects = ["ООП", "Бази даних", "Вища Математика"]
    real_scores = [85, 75, 90]
    desired_scores_for_details = [90, 80, 95]
    desired_average = 92.5

    filename_parts = {
        "ПІБ": FULL_NAME,
        "ГРУПА": GROUP,
        "НОМЕР-РОБОТИ": WORK_NUMBER
    }

    try:
        student_obj = Student(
            full_name=FULL_NAME,
            group_number=GROUP,
            birth_date=date(2003, 10, 31),
            address="м. Київ, вул. Тихого"
        )
        print(f"\n Створено об'єкт СТУДЕНТ: {student_obj.full_name}, {student_obj.group_number}")

        real_perf_obj = AcademicPerformanceImpl(subjects=subjects, scores=real_scores)
        print(f" Створено об'єкт Реальна Успішність. Середній бал: {real_perf_obj.average_score():.2f}")

        desired_perf_obj = DesiredPerformance(
            subjects=subjects,
            scores=desired_scores_for_details,
            desired_score=desired_average
        )
        print(f" Створено об'єкт Бажана Успішність. Бажаний середній бал: {desired_perf_obj.average_score():.2f}")

        # --- 3. Агрегація даних ---
        data_aggregator = StudentData(
            student=student_obj,
            real_performance=real_perf_obj,
            desired_performance=desired_perf_obj
        )
        print(" Агреговано всі дані в StudentData.")

        # --- 4. Збереження даних у різних форматах ---

        print("\n Початок збереження даних...")

        # A. Збереження у JSON
        json_saver = JSONSaver(data_aggregator, filename_parts)
        json_file = json_saver.save()
        print(f"   -> JSON: Збережено у файл: {os.path.basename(json_file)}")

        # B. Збереження у XML
        xml_saver = XMLSaver(data_aggregator, filename_parts)
        xml_file = xml_saver.save()
        print(f"   -> XML: Збережено у файл: {os.path.basename(xml_file)}")

        # C. Збереження у CSV
        csv_saver = CSVSaver(data_aggregator, filename_parts)
        csv_file = csv_saver.save()
        print(f"   -> CSV: Збережено у файл: {os.path.basename(csv_file)}")

        print("\n Усі файли успішно створено!")

    except (ValueError, TypeError, IOError, Exception) as e:
        print(f"\n Виникла критична помилка: {e}")


if __name__ == "__main__":
    main()