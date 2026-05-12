---
name: recipe-create-classroom-course
version: 1.0.0
description: |
  Cree un cours Google Classroom et envoie les invitations aux etudiants avec le role STUDENT.
  Utilise ce skill quand l'utilisateur dit : "cree un cours Google Classroom", "ouvre une classe sur Classroom", "invite mes etudiants au cours", ou demande a setup un cours scolaire avec roster.
  NE PAS utiliser pour : creer une formation TutorLMS schoolsWP (voir core/agents-py et stack TutorLMS du projet), gerer une liste de taches projet (utiliser recipe-create-task-list), ou poser un Drive Partage pour ressources de cours (utiliser recipe-create-shared-drive).
metadata:
  openclaw:
    category: "recipe"
    domain: "education"
    requires:
      bins: ["gws"]
      skills: ["gws-classroom"]
---

# Create a Google Classroom Course

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-classroom`

Create a Google Classroom course and invite students.

## Steps

1. Create the course: `gws classroom courses create --json '{"name": "Introduction to CS", "section": "Period 1", "room": "Room 101", "ownerId": "me"}'`
2. Invite a student: `gws classroom invitations create --json '{"courseId": "COURSE_ID", "userId": "student@school.edu", "role": "STUDENT"}'`
3. List enrolled students: `gws classroom courses students list --params '{"courseId": "COURSE_ID"}' --format table`

