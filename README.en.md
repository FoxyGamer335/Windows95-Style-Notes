# Super Notes in Windows 95 Style

[Русская версия](README.md)

Need notes that support not only plain text, but also markup, logic, and styling?
No?
I'm giving you all that anyway.
I made this project purely for myself, but maybe someone else will like it too.

## Features

* Move windows across an infinite canvas
* Resize windows
* Grid for positioning windows
* Zoom the workspace in and out
* Touchscreen support
* Built-in code editor
* HTML support in note content
* Ability to add CSS and JavaScript to individual notes
* Automatic state saving
* Data stored locally in the browser
* Import and export notes as JSON
* Ability to delete and rename notes
* Window stacking order changes when interacting with them

## Editor

The content is edited using [Ace Editor](https://ace.c9.io/).

The editor supports HTML syntax highlighting, autocompletion, snippets, and other Ace features.

A note's content can be plain HTML:

```html
<h2>Title</h2>
<p>Note text</p>
```

You can also use custom styles:

```html
<style>
    p {
        font-size: 20px;
    }
</style>
```

and JavaScript:

```html
<script>
    console.log("Hello!");
</script>
```

This means that an individual window can contain not only text, but also interactive elements.

## Data Saving

The workspace state is automatically saved in the browser using **IndexedDB**.

The following are saved:

* window positions;
* sizes;
* order;
* note names;
* content;
* camera zoom level;

## Import and Export

The **"Settings"** menu currently provides only:

* **Import JSON**
* **Export JSON**

This makes it possible, for example, to move a collection of notes between browsers or create backups.

## Controls

### Workspace

* **LMB / tap on an empty area** — move the workspace
* **Drag a window by its title bar** — move the window
* **Grab the bottom-right corner** — resize the window
* **Interact with a window** — bring it to the foreground
* **Two fingers on a touchscreen / mouse wheel** — zoom the workspace

## Creating a Note

Click the **"Create"** button.

A new window will appear in the center of the current camera view and will automatically open in edit mode.

In the editor, you can change:

* window name;
* content;
* HTML;
* CSS;
* JavaScript.

After confirming, the content is displayed directly inside the window.

## Technologies Used

* HTML
* CSS
* JavaScript
* IndexedDB
* Ace Editor
* Bootstrap Icons

## Data

All notes are stored locally in the device's browser.

The project does not require its own database or server-side storage for the workspace.

> **Important:** clearing browser site data may result in the loss of locally stored notes. Use JSON export for backups.

[Start Taking Notes](https://foxygamer335.github.io/Windows95-Style-Notes/)

## License

MIT License
