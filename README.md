<div align="center">
  <a href="https://github.com/activist-org/i18n-check"><img src="https://raw.githubusercontent.com/activist-org/i18n-check/main/.github/resources/i18nCheckGitHubBanner.png" width=1024 alt="i18n check logo"></a>
</div>

[![issues](https://img.shields.io/github/issues/activist-org/i18n-check?label=%20&logo=github)](https://github.com/activist-org/i18n-check/issues)
[![rtd](https://img.shields.io/readthedocs/i18n-check.svg?label=%20&logo=read-the-docs&logoColor=ffffff)](http://i18n-check.readthedocs.io/en/latest/)
[![python](https://img.shields.io/badge/Python-4B8BBE.svg?logo=python&logoColor=ffffff)](https://github.com/activist-org/i18n-check/blob/main/CONTRIBUTING.md)
[![pypi](https://img.shields.io/pypi/v/i18n-check.svg?label=%20&color=4B8BBE)](https://pypi.org/project/i18n-check/)
[![pypistatus](https://img.shields.io/pypi/status/i18n-check.svg?label=%20)](https://pypi.org/project/i18n-check/)
[![license](https://img.shields.io/github/license/activist-org/i18n-check.svg?label=%20)](https://github.com/activist-org/i18n-check/blob/main/LICENSE.txt)
[![coc](https://img.shields.io/badge/Contributor%20Covenant-ff69b4.svg)](https://github.com/activist-org/i18n-check/blob/main/.github/CODE_OF_CONDUCT.md)
[![matrix](https://img.shields.io/badge/Matrix-000000.svg?logo=matrix&logoColor=ffffff)](https://matrix.to/#/#activist_community:matrix.org)

### Check i18n/L10n keys and values

`i18n-check` is a Python package to automate the validation of keys and values of your internationalization and localization processes.

Developed by the [activist community](https://github.com/activist-org), this process is meant to assure that development and i18n/L10n teams are in sync when using JSON based localization processes. The action can be expanded later to work for other file type processes as needed.

> [!NOTE]
> For the GitHub action please see [activist-org/i18n-check-action](https://github.com/activist-org/i18n-check-action).

<a id="contents"></a>

# **Contents**

- [Conventions](#contentions-)
- [How it works](#how-it-works-)
  - [Arguments](#arguments-)
  - [Checks](#checks-)
- [Configuration](#configuration-)
- [Contributing](#contributing)
- [Environment setup](#environment-setup)
- [Contributors](#contributors-)

<a id="conventions-"></a>

# Conventions [`⇧`](#contents)

[activist](https://github.com/activist-org/activist) i18n keys follow the following conventions that are enforced by `i18n-check`:

- All key base paths should be the file path where the key is used prepended with `i18n.`
  - Starting i18n keys with a common identifier allows them to be found within checks
- If a key is used in more than one file, then the lowest common directory followed by `_global` is the base path
- Base paths should be followed by a minimally descriptive content reference
  - Only the formatting of these content references is checked via `i18n-check`
- Separate base directory paths by periods (`.`)
- Separate all directory and file name components as well as content references by underscores (`_`)
- Repeat words in file paths for sub directory organization should not be repeated in the key

> [!NOTE]
> An example valid key is:
>
> File: `components/component/ComponentName.ext`
>
> Key: `"components.component_name.CONTENT_REFERENCE"`

<a id="how-it-works-"></a>

# How it works [`⇧`](#contents)

<a id="arguments-"></a>

### Arguments [`⇧`](#contents)

You provide `i18n-check` with the following arguments:

- `src-dir`: The path to the directory that has source code to check
- `i18n-dir`: The directory path to your i18n files
- `i18n-src`: The name of the i18n source file

<a id="checks-"></a>

### Checks [`⇧`](#contents)

From there the following checks are ran across your codebase:

- `key-identifiers`: Does the source file have keys that don't match the above format or name conventions?
  - Rename them so i18n key usage is consistent and their scope is communicated in their name.
- `invalid-keys`: Does the codebase include i18n keys that are not within the source file?
  - Check their validity and resolve if they should be added to the i18n files or replaced.
- `unused-keys`: Does the source file have keys that are not used in the codebase?
  - Remove them so the localization team isn't working on strings that aren't used.
- `non-source-keys`: Do the target locale files have keys that are not in the source file?
  - Remove them as they won't be used in the application.
- `repeat-keys`: Do any of localization files have repeat keys?
  - Separate them so that the values are not mixed when they're in production.
- `repeat-values`: Does the source file have repeat values that can be combined into a single key?
  - Combine them so the localization team only needs to localize one of them.
- `nested-keys`: Do the i18n files contain nested JSON structures?
  - Flatten them to make replacing invalid keys easier and with find-and-replace.

Each of the above checks is ran in parallel with directions for how to fix the i18n files being provided when errors are raised. Checks can also be disabled in the workflow via options passed in the configuration YAML file.

<a id="configuration-"></a>

# Configuration [`⇧`](#contents)

The following details the `.18n-check.yaml` configuration file, with a further example being the [configuration file for this repository](/.i18n-check.yaml) that we use in testing.

```yaml
src-dir: frontend
i18n-dir: frontend/i18n
i18n-src: frontend/i18n/en.json

checks:
  - key-identifiers: true
  - invalid-keys: true
  - unused-keys: true
  - non-source-keys: true
  - repeat-keys: true
  - repeat-values: true
  - nested-keys: true

file-types-to-check: [.ts, .js]
directories-to-skip: [frontend/node_modules]
files-to-skip: []
warn-on-nested-keys: true
```

Common additional arguments for using specific web frameworks can be found in the dropdowns below:

<details><summary>Vue.js</summary>
<p>

```yaml
file_types_to_check: [.vue]
directories_to_skip: [.nuxt, .output, dist]
```

</p>
</details>

<a id="contributing"></a>

# Contributing [`⇧`](#contents)

<a href="https://matrix.to/#/#activist_community:matrix.org"><img src="https://raw.githubusercontent.com/activist-org/Organization/main/resources/images/logos/MatrixLogoGrey.png" height="50" alt="Public Matrix Chat" align="right"></a>

activist uses [Matrix](https://matrix.org/) for internal communication. You're more than welcome to [join us in our public chat rooms](https://matrix.to/#/#activist_community:matrix.org) to share ideas, ask questions or just say hi to the team :)

Please see the [contribution guidelines](CONTRIBUTING.md) if you are interested in contributing. Work that is in progress or could be implemented is tracked in the [issues](https://github.com/activist-org/i18n-check/issues) and [projects](https://github.com/activist-org/i18n-check/projects).

> [!NOTE]
> Just because an issue is assigned on GitHub doesn't mean the team isn't open to your contribution! Feel free to write [in the issues](https://github.com/activist-org/i18n-check/issues) and we can potentially reassign it to you.

Also check the [`-next release-`](https://github.com/activist-org/i18n-check/labels/-next%20release-) and [`-priority-`](https://github.com/activist-org/i18n-check/labels/-priority-) labels in the [issues](https://github.com/activist-org/i18n-check/issues) for those that are most important, as well as those marked [`good first issue`](https://github.com/activist-org/i18n-check/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that are tailored for first-time contributors. For those new to coding or our tech stack, we've collected [links to helpful documentation pages](CONTRIBUTING.md#learning-the-tech-stack-) in the [contribution guidelines](CONTRIBUTING.md).

We would be happy to discuss granting you further rights as a contributor after your first pull requests, with a maintainer role then being possible after continued interest in the project. activist seeks to be an inclusive, diverse and supportive organization. We'd love to have you on the team!

<a id="how-you-can-help"></a>

## How you can help [`⇧`](#contents)

- [Reporting bugs](https://github.com/activist-org/i18n-check/issues/new?assignees=&labels=bug&template=bug_report.yml) as they're found 🐞
- Working with us on [new features](https://github.com/activist-org/i18n-check/issues?q=is%3Aissue+is%3Aopen+label%3Afeature) ✨
- [Documentation](https://github.com/activist-org/i18n-check/issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation) for onboarding and project cohesion 📝

<a id="environment-setup"></a>

# Environment setup [`⇧`](#contents)

1. First and foremost, please see the suggested IDE setup in the dropdown below to make sure that your editor is ready for development.

> [!IMPORTANT]
>
> <details><summary>Suggested IDE setup</summary>
>
> <p>
>
> VS Code
>
> Install the following extensions:
>
> - [charliermarsh.ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
> - [streetsidesoftware.code-spell-checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
>
> </p>
> </details>

2. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the [i18n-check repo](https://github.com/activist-org/i18n-check), clone your fork, and configure the remotes:

> [!NOTE]
>
> <details><summary>Consider using SSH</summary>
>
> <p>
>
> Alternatively to using HTTPS as in the instructions below, consider SSH to interact with GitHub from the terminal. SSH allows you to connect without a user-pass authentication flow.
>
> To run git commands with SSH, remember then to substitute the HTTPS URL, `https://github.com/...`, with the SSH one, `git@github.com:...`.
>
> - e.g. Cloning now becomes `git clone git@github.com:<your-username>/i18n-check.git`
>
> GitHub also has their documentation on how to [Generate a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 🔑
>
> </p>
> </details>

```bash
# Clone your fork of the repo into the current directory.
git clone https://github.com/<your-username>/i18n-check.git
# Navigate to the newly cloned directory.
cd i18n-check
# Assign the original repo to a remote called "upstream".
git remote add upstream https://github.com/activist-org/i18n-check.git
```

- Now, if you run `git remote -v` you should see two remote repositories named:
  - `origin` (forked repository)
  - `upstream` (i18n-check repository)

3. Create a virtual environment, activate it and install dependencies:

   ```bash
   # Unix or MacOS:
   python3 -m venv venv
   source venv/bin/activate

   # Windows:
   python -m venv venv
   venv\Scripts\activate.bat

   # After activating venv:
   pip install --upgrade pip
   pip install -r requirements-dev.txt

   # To install the CLI for local development:
   pip install -e .
   ```

You're now ready to work on `i18n-check`!

> [!NOTE]
> Feel free to contact the team in the [Development room on Matrix](https://matrix.to/#/!CRgLpGeOBNwxYCtqmK:matrix.org?via=matrix.org&via=acter.global&via=chat.0x7cd.xyz) if you're having problems getting your environment setup!

<a id="contributors-"></a>

# Contributors [`⇧`](#contents)

Thanks to all our amazing [contributors](https://github.com/activist-org/i18n-check/graphs/contributors)! ❤️

<a href="https://github.com/activist-org/i18n-check/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=activist-org/i18n-check" />
</a>
