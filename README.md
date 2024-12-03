# ScopeFoundry website in Hugo


Built off of the [Docsy example template](https://github.com/google/docsy-example)



## Prerequisites

The following are basic prerequisites for using Docsy taken from the [official Docsy repo](https://github.com/google/docsy):

- Install a recent release of the Hugo "extended" version. If you install from
  the [Hugo release page](https://github.com/gohugoio/hugo/releases), make sure
  you download the `extended` version, which supports SCSS.

- Install `PostCSS` so that the site build can create the final CSS assets. You
  can install it locally by running the following commands from the root
  directory of your project:

  ```sh
  npm install --save-dev autoprefixer
  npm install --save-dev postcss-cli
  ```

  Starting in
  [version 8 of `postcss-cli`](https://github.com/postcss/postcss-cli/blob/master/CHANGELOG.md),
  you must also separately install `postcss`:

  ```sh
  npm install -D postcss
  ```

Any additional prerequisites depend on the
[installation option](https://www.docsy.dev/docs/get-started/#installation-options)
you choose. We recommend using Docsy as a Hugo module, which requires that you
have the Go language installed in addition to Hugo and PostCSS.

For complete prerequisites and instructions, see our
[Get started guides](https://www.docsy.dev/docs/get-started/).


## Running the website locally

Once you've made your working copy of the site repo, from the repo root folder, run:

```bash
hugo server
```


## Troubleshooting

As you run the website locally, you may run into the following error:

```console
$ hugo server
WARN 2023/06/27 16:59:06 Module "project" is not compatible with this Hugo version; run "hugo mod graph" for more information.
Start building sites …
hugo v0.101.0-466fa43c16709b4483689930a4f9ac8add5c9f66+extended windows/amd64 BuildDate=2022-06-16T07:09:16Z VendorInfo=gohugoio
Error: Error building site: "C:\Users\foo\path\to\docsy-example\content\en\_index.md:5:1": failed to extract shortcode: template for shortcode "blocks/cover" not found
Built in 27 ms
```

This error occurs if you are running an outdated version of Hugo. As of docsy theme version `v0.7.0`, hugo version `0.110.0` or higher is required.
See this [section](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/#install-hugo) of the user guide for instructions on how to install Hugo.

Or you may be confronted with the following error:

```console
$ hugo server

INFO 2021/01/21 21:07:55 Using config file:
Building sites … INFO 2021/01/21 21:07:55 syncing static files to /
Built in 288 ms
Error: Error building site: TOCSS: failed to transform "scss/main.scss" (text/x-scss): resource "scss/scss/main.scss_9fadf33d895a46083cdd64396b57ef68" not found in file cache
```

This error occurs if you have not installed the extended version of Hugo.
See this [section](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/#install-hugo) of the user guide for instructions on how to install Hugo.

Or you may encounter the following error:

```console
$ hugo server

Error: failed to download modules: binary with name "go" not found
```

This error occurs if you have not installed the `go` programming language on your system.
See this [section](https://www.docsy.dev/docs/get-started/docsy-as-module/installation-prerequisites/#install-go-language) of the user guide for instructions on how to install `go`.


[alternate dashboard]: https://app.netlify.com/sites/goldydocs/deploys
[deploys]: https://app.netlify.com/sites/docsy-example/deploys
[Docsy user guide]: https://docsy.dev/docs
[Docsy]: https://github.com/google/docsy
[example.docsy.dev]: https://example.docsy.dev
[Hugo theme module]: https://gohugo.io/hugo-modules/use-modules/#use-a-module-for-a-theme
[Netlify]: https://netlify.com
[Docker Compose documentation]: https://docs.docker.com/compose/gettingstarted/
