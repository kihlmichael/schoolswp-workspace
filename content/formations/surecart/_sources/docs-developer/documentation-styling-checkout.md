---
source_url: https://developer.surecart.com/documentation/styling/checkout
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/styling/checkout#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart checkout components use a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM) to encapsulate their styles. This protects against style conflicts and keeps components stable as internal HTML structure evolves.

Two customization methods: **CSS custom properties (variables)** for global style changes and **CSS parts** for fine-grained component styling.

## [​](https://developer.surecart.com/documentation/styling/checkout#css-variables) CSS Variables

Scope to `:root:root` to ensure specificity inside shadow DOM:

```
:root:root {
  /** Remove all border radiuses */
  --sc-border-radius-small: 0;
  --sc-border-radius-medium: 0;
  --sc-border-radius-large: 0;
  --sc-border-radius-x-large: 0;
}
```

### Key variable groups

**Colors:** `--sc-color-primary-500`, `--sc-color-gray-{50-950}`, `--sc-color-neutral-{50-950}`, `--sc-color-success-{50-950}`, `--sc-color-info-{50-950}`, `--sc-color-warning-{50-950}`, `--sc-color-danger-{50-950}`

**Border Radius:** `--sc-border-radius-small`, `--sc-border-radius-medium`, `--sc-border-radius-large`, `--sc-border-radius-x-large`, `--sc-border-radius-circle`, `--sc-border-radius-pill`

**Spacing:** `--sc-spacing-{xxx-small through xxxx-large}`

**Typography:** `--sc-font-sans`, `--sc-font-size-{xx-small through xxxx-large}`, `--sc-font-weight-{light/normal/semibold/bold}`

**Inputs:** `--sc-input-height-{small/medium/large}`, `--sc-input-border-color`, `--sc-input-border-color-focus`, `--sc-input-background-color`, etc.

## [​](https://developer.surecart.com/documentation/styling/checkout#css-parts) CSS Parts

CSS Parts allow targeting specific parts of a component's shadow DOM using `::part()`. Find available parts in the [Components Documentation](https://components.surecart.com/) under "Shadow Parts" for each component.

### Input/Text Field example

```
sc-input {
  --sc-font-sans: monospace;
  --sc-color-primary-500: #2dd4bf;
}
sc-input::part(base) {
  border: 1px solid black;
  box-shadow: 2px 2px #2dd4bf;
  border-radius: 0;
}
sc-input::part(label) {
  color: black;
  font-size: 14px;
  letter-spacing: 2px;
  text-transform: uppercase;
}
sc-input::part(base):hover {
  box-shadow: 5px 5px #2dd4bf;
}
```

### Button example

```
sc-button::part(base) {
  border-radius: 0;
  background: white;
  font-family: monospace;
  border: 1px solid black;
  box-shadow: 2px 2px #2dd4bf;
  color: black;
}
sc-button::part(base):hover {
  background: #2dd4bf;
}
```

### Shipping Address example

```
sc-order-shipping-address {
  --sc-font-sans: monospace;
  --sc-address-column-spacing: 1em;
  --sc-color-primary-500: #2dd4bf;
}
sc-order-shipping-address::part(input__base),
sc-order-shipping-address::part(select__base) {
  border: 1px solid black;
  border-radius: 0;
  box-shadow: 2px 2px #2dd4bf;
}
```
