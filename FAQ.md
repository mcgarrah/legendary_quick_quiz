# Frequently Asked Questions

- [Frequently Asked Questions](#frequently-asked-questions)
  - [Hosted Application Stopped; How do I start it?](#hosted-application-stopped-how-do-i-start-it)
  - [Hosted Application HTTP Error 404](#hosted-application-http-error-404)
  - [No questions are loaded; How do I load them?](#no-questions-are-loaded-how-do-i-load-them)
  - [Do I retain any questions uploaded?](#do-i-retain-any-questions-uploaded)
  - [Can I use Markdown or HTML in the Question fields?](#can-i-use-markdown-or-html-in-the-question-fields)
  - [Have a question not answered](#have-a-question-not-answered)

## Hosted Application Stopped; How do I start it?

![Ploomber Stopped WebApp](static/images/ploomber-stopped.png)

If this application shows a screen that the application is not running, just press the button to start it up and it should start in a minute or so. This is expected behavior for the free tier of [Ploomber](https://ploomber.io/). And thanks for the free hosting.

## Hosted Application HTTP Error 404

[Ploomber](https://ploomber.io/) is a newer service with some innovative bleeding edge features. Sometime there is blood involved in the hosting. If the website is not up, file an [issue in the repository](https://github.com/mcgarrah/legendary_quick_quiz/issues/new/choose) and pick "Bug report".

## No questions are loaded; How do I load them?

~~In the **Settings** page, there is a section with buttons to Import, Export and Clear the Questions. By not selecting a JSON file on that page, it will automatically, load the `initial_questions.json` file from the webroot directory.~~

Someone likely pressed "Clear Questions" on the Settings page. Go to "Settings" and press the "Import Questions" to reload the default questions or use the option to upload a JSON file to import Questions.

## Do I retain any questions uploaded?

No. The SQLite database hosting the contents is dumped on every deployment. No backups are kept with our hosting provider either.

## Can I use Markdown or HTML in the Question fields?

Not at this time. There is no provision for passing HTML or other presentation attributes thru for display.

There is a TODO item to investigate MarkDown and MathJAX as options but it lower on my list of things to do right now.

## Have a question not answered

Try out our [Github Issues](https://github.com/mcgarrah/legendary_quick_quiz/issues/new/choose) for the project to ask and I will see about getting it addressed.

Copyright © 2024 J. Michael McGarrah <mcgarrah@gmail.com>
