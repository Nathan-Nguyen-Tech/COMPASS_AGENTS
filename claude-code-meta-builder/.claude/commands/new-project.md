---
description: Create a new Claude Code project with optimal configuration
argument-hint: [project-type] [project-name] [additional-requirements]
---

Create a new Claude Code project with the following specifications:

**Project Type**: $1
**Project Name**: $2
**Additional Requirements**: $3

Please use the project-creator agent to:

1. **Analyze Requirements**
   - Understand the project type and specific needs
   - Ask clarifying questions about technology stack preferences
   - Identify security and compliance requirements
   - Determine team size and collaboration needs

2. **Generate Project Structure**
   - Create optimal folder organization for the project type
   - Set up appropriate configuration files
   - Include necessary build and deployment configurations
   - Establish clear naming conventions

3. **Configure Claude Code Integration**
   - Create comprehensive CLAUDE.md with project context
   - Set up security permissions appropriate for the project
   - Configure useful hooks for formatting and linting
   - Include relevant agents for common project tasks
   - Add helpful slash commands for frequent workflows

4. **Essential Documentation**
   - Generate README with setup and usage instructions
   - Create development guidelines and coding standards
   - Include architecture overview and design decisions
   - Add deployment and maintenance documentation

5. **Development Environment**
   - Set up package management and dependencies
   - Configure testing framework with example tests
   - Include environment variable templates
   - Set up development and build scripts

Ensure the project follows current Claude Code best practices and includes all security configurations to protect sensitive files and operations.