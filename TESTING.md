# Manual and Automated Testing

Both manual and automated testing were crucial in ensuring my website was functional. Manual testing ensured all features worked as intended. This included testing booking, editing, and canceling court bookings. This was tested from the user login and admin side. It verifies usability, detects interface issues, and confirms workflow logic. By simulating real user interactions such as creating an account, making court bookings, it helps identify bugs, improve user experience, and ensure the site meets functional requirements.

I also performed some automated testing on the forms, models, views and urls. This helped to verify that each component of the tennis booking website functions as expected. They quickly ensure data integrity, validate routing, and confirm form behavior. The use of automated testing increases reliability and reduces the risk of introducing bugs during updates or new feature additions.

# Table of Contents

- [Code Validation](#code-validation)
- [Lighthouse](#lighthouse-testing)
- [Responsiveness](#responsiveness-testing)
- [Browser Compatibility](#browser-compatibilty-testing)
- [User Stories](#user-story-testing)

## Code Validation

### HTML

The HTML validator reports errors due to Django template tags like `{% load static %}` and `{% block title %}`. These tags are not standard HTML, so the validator flags them as invalid. In practice, the template renders correctly in Django, making these validation errors harmless and expected.
