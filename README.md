# Play Tennis

Play Tennis is a full-stack, responsive website built for a fictional tennis court booking system for tennis players of all levels.

The website consists of a homepage which allow introduces the club and allows users to book from the homepage. There is also sign up page which allows users to create an account and start making court bookings. Once users have logged in, they can manage their court bookings.

<p align="center">
  <img src="booking/static/booking/images/responsiveness.png" alt="Website appearance on all devices">
</p>

## Table of Contents

- [Overview](#overview)
- [Agile Methodology](#agile-methodology)
- [User Experience (UX)](#user-experience-ux)
  - [Goals](#goals)
  - [User Stories](#user-stories)
  - [Visual Design](#visual-design)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [languages](#Languages)
  - [Frameworks](#frameworks)
  - [Libraries](#libraries)
  - [Platforms](#platforms)
  - [Other tools](#other-tools)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

# Overview

The Play Tennis website is a responsive applications which functions seemlessly on small screens as on your desktop. The website allows users to book from a range of different tennis courts. The website is for tennis players of all levels and uses the Bootstrap front end framework and the Django web application framework.

# Agile Methodology

I used the Agile methodology focussing on planning the project in iterative cycles and placing the different user stories under different epic headings.

The planning of the project was a fluid process as my user stories, which contained acceptance criteria and tasks, scope was initially too big and they needed to be broken down into smaller user stories.

The [MoSCoW Method of Prioritisation](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html) was also used. This proved to be a vital tool in priritising the importance of each user story because dividing them up into "Must Have's", "Should Have's", "Could Have's" and "Won't Have's". This provided a clear direction with a large focus on ensuring the "Must Have's" were achieved and the "Won't Have's" providing ideas on the development of the website in the future but not to be achieved at this stage. In other words, the user stories were written to achieve the Minimum Viable Product(MVP).

<details>
<summary>Here are screenshots of my Kanban Board below:</summary>

![Kanband: Kanban board](booking/static/booking/images/kanban_board_layout.png)

![Kanband: list of issues](booking/static/booking/images/issues.png)

</details>

Each user story was also placed under an Epic title of one of Admin Management, Booking System, Security and Validation, Court Management, User Authentication and Profiles or User Interface and Experience. This helped organize the tasks and ensured alignment with objectives.

# User Experience

## Goals

Play Tennis aims to provide a platform where tennis players can manage their bookings for tennis courts at the local club. Visitors are given an introduction to the club and the address is listed in the footer. The button to book courts features prominently on the homepage in both the navbar and on the main image of the site.

## User Stories

Each User Story was recorded in [GitHub Issues](https://github.com/David5p/play_tennis/issues). I edited my user stories during the project. My mentor recommended that I elaborate on some of my user stories and break them down into smaller user stories. For instance one of my user stories was originally, "As a user, I want to be able to login and logout of my account." This user story contained lots of different tasks and as you can see below, I broke it down into smaller user stories where more detail was able to be included.

- As a new user, I want to register with an email, username, and password so that I can create an account.

- As a registered user, I want to log in with my credentials so that I can access my account and book courts.

- As a logged-in user, I want to log out securely so that no one else can access my account.

- As a user, I want my password stored securely so that my account remains safe.

- As a user, I want to search for courts by name, location, or type so that I can find the courts I want to play on.

- As a user, I want to cancel a booking before its scheduled start time so that I don’t occupy the slot unnecessarily.

- As a user, I want cancelled bookings to free up the time slot so that other users can book it.

- As a user, I want to see a list of all my bookings so that I know what reservations I have.

- As a user, I want each booking to show the court, date, and time so that I can see all relevant details at a glance.

- As a user, I want the booking history page to be styled clearly so that I can easily read and understand my bookings.

- As a user, I want the website to have a consistent and modern design so that it feels professional and easy to use.

- As a user, I want the website to work well on mobile, tablet, and desktop devices so that I can book courts anywhere.

- As a user, I want an intuitive navigation system so that I can easily find booking, login, and profile pages.

- As a user I can receive an email notification after bookings and cancellations so that I have a record.

- As a user I can pay for bookings online so that I don't have to pay at the venue.

- As a user I can log in with my Google or Facebook account so that I don't need a separate password.

- As a user I can book courtsthrough a mobile app so that I can access the platform on the go.

- As an admin, I want to extend the Court model with location and type so that users can filter courts effectively.

- As an admin, I want to add and edit courts so that I can maintain accurate court information.

- As an admin, I want to define available time slots for each court so that users can book them.

- As an admin, I want to delete or modify bookings so that I can manage user reservations.

- As an admin, I want to filter bookings by date, court, or user so that I can quickly find relevant reservations.
