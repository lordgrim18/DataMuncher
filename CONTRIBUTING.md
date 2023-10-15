## Contributing to DataMuncher

We welcome contributions from everyone, regardless of your experience level. Here are some ways you can contribute:

* **Add new features.** We are also open to suggestions for new features. If you have an idea for a new feature, please open an issue and describe your proposal.
* **Fix bugs.** We are always looking for people to help us fix bugs in our code. If you find a bug, please open an issue and provide a detailed description of the problem.
* **Improve documentation.** Our documentation is always in need of improvement. If you find any errors or omissions in the documentation, please open an issue and submit a pull request to fix them.


   ### Creating issues
- Before working on anything ensure that you open an issue describing about the work you will be doing.
- 4 issue templates are present which can be used to create your issue.
- The issue templates present are
  - Bug Report : for reporting any bugs found in the code.
  - Documentation Issue : for reporting any issues/changes to be made in the documentation.
  - Feature Request : for requesting any new features to be added.
  - Code Optimization : for reporting any code optimization that can be done.
- The required details are asked in the corresponding template and can be filled there.
- If you feel that your work doesn't match any of the templates then create a blank issue.
- In case of blank issue ensure that proper description is given. 


   ## Getting Started
  
1. **Fork the Repository**: Click the "Fork" button on the top right of the repository's page.
2. **Clone Your Fork**: Open your terminal and run the following command, replacing `[your-username]` with your GitHub username:

   ```bash
   git clone https://github.com/[your-username]/DataMuncher.git
3. **Create a Branch**: Create a new branch for your feature or bug fix: `git checkout -b feature-name`
4. **Make Changes**: Make your changes or additions to the code.
5. **Testing**: Make sure to test your changes thoroughly.
6. **Commit Your Changes**: Commit your changes with a descriptive commit message. The format of to be followed for commit messages is given below.
7. **Push Your Changes**: Push your changes to your forked repository.
8. **Open a Pull Request**: Create a pull request from your forked repository to this repository.
10. **Describe Your Pull Request**: A template has already been made for the pull request. Fill the required details such as description of your changes, what you've added, and any relevant information for reviewers. You also need to replace the <ticket_number> with the ticket number of the issue that you opened/assigned to.


   ## Commit Message Format
   
   Each commit message consists of a **header** and a **subject**. The header has a special format that includes a **type** and a **scope** :
   ```
   <type>(<scope>): <subject>
   ```
   
   The **header** is mandatory and the **scope** of the header is optional.
   
   Example — `fix: remove unused dependency lodash.camelcase`
   
   Any line of the commit message cannot be longer 100 characters. This allows the message to be easier to read on GitHub as well as in various git tools.
   
   #### Type
   Must be one of the following:
   
   * **feat**: A new feature.
   * **fix**: A bug fix.
   * **docs**: Documentation only changes.
   * **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
   * **refactor**: A code change that neither fixes a bug nor adds a feature.
   * **perf**: A code change that improves performance.
   * **test**: Adding missing tests.
   * **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation.
   
   #### Scope
   The scope is optional and could be anything specifying place of the commit change. For example `linux`, some file, etc...
   
   #### Subject
   The subject contains succinct description of the change:
   
   * use the imperative, present tense: `change` not `changed` nor `changes`,
   * don't capitalize first letter,
   * no dot (.) at the end.
        
   A detailed explanation can be found in this [document](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#).

### Some things to keep in mind

1. Before pushing your changes to the remote repo ensure that it is synched with the latest changes.
2. Make sure that the changes you made locally have been committed.
3. Pull the updated content from the main branch.

   ```bash
   git pull origin main
4. Resolve any conflicts if present.
5. Now push the branch on which you were working on.
   ```bash
   git push origin branch-name
6. Go to your repo and open a pull request.


## Contact

If you have any questions about contributing to this project, please feel free to open an issue or contact me at jeromjomanthara@gmail.com.
