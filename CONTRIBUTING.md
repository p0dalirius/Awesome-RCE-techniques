# Introduction

### Welcome contributiors!

>First off, thank you for considering contributing to Awesome-RCE-techniques. It's people like you that make Awesome-RCE-techniques such a great ressource.

### Our guidelines.

>Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved. Awesome-RCE-techniques is a compilation of code exectution techniques that aims to be the most comprehansive and beginner friendly.

### Contributions we are looking for.

Documentating all the RCE techniques is a time consuming process, you can help by : 

> * Reporting an application that isn't covered by the documentation. Consider adding all the informations you got to help 
the team (github page, version, screenshot, documentation, walkthrough...)
> * Writing a step-by-step documentation.
> * Providing test environnment to train these Remote Code Execution (RCE) techniques.

### Contributions we are NOT looking for.

> Please, don't use the issue tracker for support questions. If you can't figure out how to RCE an application, feel free to check this ressources : 
> * The Hacker Recipes (https://www.thehacker.recipes/)
> * HackTricks (https://book.hacktricks.xyz/welcome/readme)
> * Payloads All The Things (https://github.com/swisskyrepo/PayloadsAllTheThings)


# Community Code of Conduct
### Be respectful

This community and its members treat one another with respect. Everyone can make a valuable contribution to Awesome-RCE-techniques. We may not always agree, but disagreement is no excuse for poor behavior and poor manners. We might all experience some frustration now and then, but we cannot allow that frustration to turn into a personal attack. It's important to remember that a community where people feel uncomfortable or threatened isn't a productive one. We expect members of the community to be respectful when dealing with other contributors as well as with people outside the Awesome-RCE-techniques project and with users of this documentation.

### Be collaborative

Collaboration is central to the free software community. We should always be open to collaboration. Your work should be done
transparently and patches should be given back to the community when they're made, not just when the distribution releases. If you wish to work on new code for existing upstream projects, at least keep those projects informed of your ideas and progress. It many not be possible to get consensus from upstream, or even from your colleagues about the correct implementation for an idea, so don't feel obliged to have that agreement before you begin, but at least keep the outside world informed of your work, and publish your work in a way that allows outsiders to test, discuss, and contribute to your efforts.

### When you disagree, consult others

Disagreements, both political and technical, happen all the time and the Celery community is no exception. It's important that we resolve disagreements and differing views constructively and with the help of the community and community process. If you really want to go a different way, then we encourage you to make a derivative distribution or alternate set of packages that still build on the work we've done to utilize as common of a core as possible.

### When you're unsure, ask for help

Nobody knows everything, and nobody is expected to be perfect. Asking questions avoids many problems down the road, and so questions are encouraged. Those who are asked questions should be responsive and helpful. However, when asking a question, care must be taken to do so in an appropriate forum.

### Step down considerately

Developers on every project come and go and here is no different. When you leave or disengage from the project, in whole or in part, we ask that you do so in a way that minimizes disruption to the project. This means you should tell people you're leaving and take the proper steps to ensure that others can pick up where you left off.

[source: [Celery](https://github.com/celery/celery/blob/master/CONTRIBUTING.rst#community-code-of-conduct) 

# Your First Contribution

> Unsure where to begin contributing to Awesome-RCE-techniques? You can start by looking through these beginner and help-wanted issues:
> Beginner issues - issues which should only require a few lines of code, and a test or two.
> Help wanted issues - issues which should be a bit more involved than beginner issues.
> Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

[source: [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md#your-first-code-contribution)] **Need more inspiration?** [1] [Read the Docs](http://docs.readthedocs.org/en/latest/contribute.html#contributing-to-development) [2] [Django](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/#first-steps) (scroll down to "Guidelines" as well)

### You never contributed to an open source project ?
Here are a couple of friendly tutorials: http://makeapullrequest.com/ and http://www.firsttimersonly.com/

> Working on your first Pull Request? You can learn how from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

[source: [React](https://github.com/facebook/react/blob/master/CONTRIBUTING.md#pull-requests)]  

As a side note, it helps to use newcomer-friendly language throughout the rest of your document. Here are a couple of examples from [Active Admin](https://github.com/activeadmin/activeadmin/blob/master/CONTRIBUTING.md):

>At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first :smile_cat:
>
>If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

# Getting started
### Give them a quick walkthrough of how to submit a contribution.
How you write this is up to you, but some things you may want to include:

>For something that is bigger than a one or two line fix:

>1. Create your own fork of the code
>2. Do the changes in your fork
>3. If you like the change and think the project could use it:
    * Be sure you have followed the code style for the project.
    * Sign the Contributor License Agreement, CLA, with the jQuery Foundation.
    * Note the jQuery Foundation Code of Conduct.
    * Send a pull request indicating that you have a CLA on file.

[source: [Requirejs](http://requirejs.org/docs/contributing.html)] **Need more inspiration?** [1] [Active Admin](https://github.com/activeadmin/activeadmin/blob/master/CONTRIBUTING.md#1-where-do-i-go-from-here) [2] [Node.js](https://github.com/nodejs/node/blob/master/CONTRIBUTING.md#code-contributions) [3] [Ember.js](https://github.com/emberjs/ember.js/blob/master/CONTRIBUTING.md#pull-requests)

### If you have a different process for small or "obvious" fixes, let them know.

> Small contributions such as fixing spelling errors, where the content is small enough to not be considered intellectual property, can be submitted by a contributor as a patch, without a CLA.
>
>As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality or creative thinking. As long as the change does not affect functionality, some likely examples include the following:
>* Spelling / grammar fixes
>* Typo correction, white space and formatting changes
>* Comment clean up
>* Bug fixes that change default return values or error codes stored in constants
>* Adding logging messages or debugging output
>* Changes to ‘metadata’ files like Gemfile, .gitignore, build scripts, etc.
>* Moving source files from one directory or package to another

[source: [Chef](https://github.com/chef/chef/blob/master/CONTRIBUTING.md#chef-obvious-fix-policy)] **Need more inspiration?** [1] [Puppet](https://github.com/puppetlabs/puppet/blob/master/CONTRIBUTING.md#making-trivial-changes)

# How to report a bug
### Explain security disclosures first!
At bare minimum, include this sentence:
> If you find a security vulnerability, do NOT open an issue. Email XXXX instead.

If you don’t want to use your personal contact information, set up a “security@” email address. Larger projects might have more formal processes for disclosing security, including encrypted communication. (Disclosure: I am not a security expert.)

> Any security issues should be submitted directly to security@travis-ci.org
> In order to determine whether you are dealing with a security issue, ask yourself these two questions:
> * Can I access something that's not mine, or something I shouldn't have access to?
> * Can I disable something for other people?
>
> If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure, just email us at security@travis-ci.org.

[source: [Travis CI](https://github.com/travis-ci/travis-ci/blob/master/CONTRIBUTING.md)] **Need more inspiration?** [1] [Celery](https://github.com/celery/celery/blob/master/CONTRIBUTING.rst#security) [2] [Express.js](https://github.com/expressjs/express/blob/master/Security.md)

### Tell your contributors how to file a bug report.
You can even include a template so people can just copy-paste (again, less work for you).

> When filing an issue, make sure to answer these questions:
>
> 1. What operating system and processor architecture are you using?
> 2. What did you do?
> 3. What did you expect to see?
> 4. What did you see instead?

[source: [Go](https://github.com/golang/go/blob/master/CONTRIBUTING.md#filing-issues)] **Need more inspiration?** [1] [Celery](https://github.com/celery/celery/blob/master/CONTRIBUTING.rst#other-bugs ) [2] [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md#reporting-bugs) (includes template)

# How to suggest a feature or enhancement
### If you have a particular roadmap, goals, or philosophy for development, share it here.
This information will give contributors context before they make suggestions that may not align with the project’s needs.

> The Express philosophy is to provide small, robust tooling for HTTP servers, making it a great solution for single page applications, web sites, hybrids, or public HTTP APIs.
>
> Express does not force you to use any specific ORM or template engine. With support for over 14 template engines via Consolidate.js, you can quickly craft your perfect framework.

[source: [Express](https://github.com/expressjs/express#philosophy)] **Need more inspiration?** [Active Admin](https://github.com/activeadmin/activeadmin#goals)

### Explain your desired process for suggesting a feature.
If there is back-and-forth or signoff required, say so. Ask them to scope the feature, thinking through why it’s needed and how it might work.

> If you find yourself wishing for a feature that doesn't exist in Elasticsearch, you are probably not alone. There are bound to be others out there with similar needs. Many of the features that Elasticsearch has today have been added because our users saw the need. Open an issue on our issues list on GitHub which describes the feature you would like to see, why you need it, and how it should work.

[source: [Elasticsearch](https://github.com/elastic/elasticsearch/blob/master/CONTRIBUTING.md#feature-requests)] **Need more inspiration?** [1] [Hoodie](https://github.com/hoodiehq/hoodie/blob/master/CONTRIBUTING.md#feature-requests) [2] [Ember.js](https://github.com/emberjs/ember.js/blob/master/CONTRIBUTING.md#requesting-a-feature)

# Code review process
### Explain how a contribution gets accepted after it’s been submitted.
Who reviews it? Who needs to sign off before it’s accepted? When should a contributor expect to hear from you? How can contributors get commit access, if at all?

> The core team looks at Pull Requests on a regular basis in a weekly triage meeting that we hold in a public Google Hangout. The hangout is announced in the weekly status updates that are sent to the puppet-dev list. Notes are posted to the Puppet Community community-triage repo and include a link to a YouTube recording of the hangout.
> After feedback has been given we expect responses within two weeks. After two weeks we may close the pull request if it isn't showing any activity.

[source: [Puppet](https://github.com/puppetlabs/puppet/blob/master/CONTRIBUTING.md#submitting-changes)] **Need more inspiration?** [1] [Meteor](https://meteor.hackpad.com/Responding-to-GitHub-Issues-SKE2u3tkSiH ) [2] [Express.js](https://github.com/expressjs/express/blob/master/Contributing.md#becoming-a-committer)

# Community

> You can chat with the team on Discord.