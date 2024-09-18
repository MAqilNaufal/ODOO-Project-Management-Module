# Odoo Project Management Module

This is a custom **Project Management Module** built for Odoo, designed to manage projects, tasks, subtasks, and milestones efficiently. The module integrates with Odoo's core framework and adds functionalities such as task dependencies, milestone tracking, and project-specific reporting.

## Features

- **Project Management**: Create, edit, and manage projects with associated tasks and milestones.
- **Task Management**: Organize tasks under different projects with support for task hierarchies (subtasks).
- **Milestones**: Define and track key milestones within projects.
- **Access Control**: Configurable access rights for project and task management.

## Installation

1. Clone this repository to your Odoo installation:
   ```bash
   git clone https://github.com/MAqilNaufal/ODOO-Project-Management-Module.git

2. Copy the project_management folder to your Odoo addons directory:
   ```bash   
   cp -r project_management /path/to/odoo/addons/

3. Update your Odoo instance:
   ```bash
   ./odoo-bin -u all

4. Activate the module through the Odoo interface:
- Go to Apps.
- Search for Project Management Module.
- Click Install.

## Configuration
To configure access control and permissions, modify the ir.model.access.csv file in the security folder. The following access rights are available:
- Read
- Write
- Create
- Unlink (delete)

## Usage
1. Creating a Project:
- Navigate to the Project Management app.
- Click Create to set up a new project with its associated tasks and milestones.

2. Managing Tasks:
- Within a project, create tasks and subtasks.
- Assign tasks to specific users and link them to project milestones.

3. Tracking Milestones:
- Use milestones to track project progress and ensure timely delivery.
- Define multiple milestones for each project.

## Contributing
If you wish to contribute to this project, fork the repository, create a new branch, and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Authors
M Aqil Naufal - Initial development of the Project Management Module.
