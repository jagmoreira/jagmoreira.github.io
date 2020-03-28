Title: I wrote a LaTeX CV template!
Date: 2017-06-23
Category: Development
Tags: latex, resume
Summary: Presenting the Friggen-Awesome LaTeX template for your CV or resumé.

I'm currently in the job market looking for a data science-related job. The first step (of many) in applying for a job is polishing up that resumé. It had been a while since I touched my resumé. I had a Word document that was 3-pages long describing in great detail all my *academic* accomplishments. While I am of course proud of my publication record and all my conference participations, it was time to actually create a 1-page resumé highlighting my *professional* experience and *skills* instead.

I had been thinking for a while about creating a LaTeX CV/resumé, so this was the perfect opportunity to finally do it. I looked around for existing templates.  is a great website with tons of templates. It even has an online editor so you don't have to install LaTeX on you computer to write your CV.

The most appealing template I found was the [Fancy CV](https://www.sharelatex.com/templates/cv-or-resume/fancy-cv), also called by Friggeri CV, originally released by [Adrian Friggeri](https://github.com/afriggeri):

![Original Fancy CV]({static}/images/fanci_cv.png)

While the original template is no longer on GitHub, many people have created their own version. Most notably, [Nadorrano](https://github.com/Nadorrano) created [CV-Friggeri-X](https://github.com/Nadorrano/cv-friggeri-x), a variation on the original Fancy CV that uses only open source fonts and adds glyphs for contact info.

![Friggeri-X CV]({static}/images/cv_friggeri_x.png)

Now, I could have used this template to write my CV... but, I didn't like the glyphs, nor the contact info on the side. So, I did some more searching and found another really awesome template called [Awesome-CV](https://github.com/posquit0/Awesome-CV) by [posquit0](https://github.com/posquit0)

![Awesome CV]({static}/images/awesome_cv.png)

Now that is a cool header!

I knew I wanted this header but I liked the 2-column layout of the Friggeri-X template. So, I set out to create a template that did just that. After a few weeks working on and off on the template, I finally got it working.

Introducing... the [Friggen-Awesome CV](https://github.com/jagmoreira/Friggen-Awesome-CV):

![Friggen-Awesome CV]({static}/images/friggen_awesome_cv.png)

It has a 2-column layout, like the Fancy CV, and a header much like the one in the Awesome CV. It also uses only open source fonts (Roboto for text and FontAwesome for glyphs) and allows you to choose from A4 or Letter paper size. You can find more detailed info in the [template repo](https://github.com/jagmoreira/Friggen-Awesome-CV).

It was great fun creating this template. While I didn't create it from scratch, I learned a lot about LaTeX internals. Just like with any programming language, you can do a lot with LaTeX variables and conditionals. Yes there are if-statements in LaTex!

I hope this template will be of great use to others, specially those currently looking for jobs. If you find something broken, have a criticism or some suggestion for improvement, please do submit an [issue](https://github.com/jagmoreira/Friggen-Awesome-CV/issues) or [pull request](https://github.com/jagmoreira/Friggen-Awesome-CV/pulls) on GitHub.

Also, if you are reading this blog and want to learn more about me, here's my own friggen' awesome [resumé]({static}/pdfs/resume.pdf). :-)

Many thanks to [Nadorrano](https://github.com/Nadorrano) and [posquit0](https://github.com/posquit0), the creators of [CV-Friggeri-X](https://github.com/Nadorrano/cv-friggeri-x) and [Awesome-CV](https://github.com/posquit0/Awesome-CV), respectively, and also to [Adrian Friggeri](https://github.com/afriggeri) for creating the original [Fancy CV](https://www.sharelatex.com/templates/cv-or-resume/fancy-cv).
