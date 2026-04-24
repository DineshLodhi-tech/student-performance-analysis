def analyze_data(data):
    print("\nTop 5 Students:\n", data.sort_values(by='Marks', ascending=False).head())

    print("\nStudents with Marks < 50:\n", data[data['Marks'] < 50])

    print("\nStudyHours vs Marks Correlation:")
    print(data[['StudyHours', 'Marks']].corr())

    print("\nAttendance vs Marks Correlation:")
    print(data[['Attendance', 'Marks']].corr())


def group_analysis(data):
    # Attendance groups
    data['AttendanceLevel'] = data['Attendance'].apply(
        lambda x: "Low" if x < 70 else ("Medium" if x < 85 else "High")
    )

    print("\nAverage Marks by Attendance Level:")
    print(data.groupby('AttendanceLevel')['Marks'].mean())

    # Study categories
    data['StudyCategory'] = data['StudyHours'].apply(
        lambda x: "Low" if x < 4 else ("Medium" if x < 7 else "High")
    )

    print("\nAverage Marks by Study Category:")
    print(data.groupby('StudyCategory')['Marks'].mean())