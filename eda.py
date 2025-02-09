
from ydata_profiling import ProfileReport

# Load your CSV file
# file_path = 'project_2.1\Electric_vehicle_dataset.csv'  
# data = pd.read_csv(file_path)

# Generate the profile report
profile = ProfileReport(ev_df, title="YData Profiling Report", explorative=True)

# Save the report to an HTML file
output_file = "ev_report.html"
profile.to_file(output_file)

print(f"Profiling report saved to {output_file}")
