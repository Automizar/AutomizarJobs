# app/routes/job_routes.py

from flask import request, render_template, redirect, url_for
from app import app, db
from app.models.user import User
from app.services.linkedin import fetch_jobs_from_linkedin, get_all_jobs, apply_to_job


@app.route('/', methods=['GET', 'POST'])
def search_jobs():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        location = request.form.get('location')  # Capture the location input
        if keywords and location:
            keyword_list = [keyword.strip() for keyword in keywords.split(',')]
            # Pass both the keywords and the location to the fetching function
            jobs = fetch_jobs_from_linkedin(keyword_list, location)
            return render_template_string(JOB_LIST_TEMPLATE, jobs=jobs)
    return render_template_string(KEYWORD_FORM)


@app.route('/apply', methods=['POST'])
def apply_to_jobs():
    jobs_to_skip = request.form.getlist('job_to_skip')  # Get the list of jobs to skip

    # Fetch all available jobs (assuming you have a function for this)
    all_jobs = get_all_jobs()  # This function should return a list of job IDs or similar identifiers

    if jobs_to_skip:
        # Convert job indices to integers
        jobs_to_skip = [int(idx) for idx in jobs_to_skip]
        print(f"Skipping jobs: {jobs_to_skip}")

        # Filter out the jobs to skip
        jobs_to_apply = [job for job in all_jobs if job not in jobs_to_skip]

        # Apply to the filtered list of jobs
        for job in jobs_to_apply:
            apply_to_job(job)  # Assuming you have a function to apply to a single job

    else:
        print("Applying to all jobs!")
        # Apply to all jobs
        for job in all_jobs:
            apply_to_job(job)

    # After processing, you can redirect to a new page or confirm the action to the user
    return 'Applied to selected jobs!'  # or render a template with confirmation message


@app.route('/user', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'POST':
        # Create a new User object
        user = User(
            first_name=request.form['first_name'],
            middle_name=request.form.get('middle_name', ''),  # Optional
            last_name=request.form['last_name'],
            experiences=request.form.getlist('experiences'),  # List of experiences
            educations=request.form.getlist('educations'),  # List of educations
            email=request.form['email'],
            address=request.form['address'],
            phone_number=request.form['phone_number']
        )

        # Add user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('search_jobs'))  # Redirect to the job search page

    return render_template('user_form.html')  # Render the user profile form