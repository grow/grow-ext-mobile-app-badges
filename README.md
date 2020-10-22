# grow-ext-mobile-app-badges

[![Build Status](https://travis-ci.org/grow/grow-ext-mobile-app-badges.svg?branch=master)](https://travis-ci.org/grow/grow-ext-mobile-app-badges)

An extension to simplify usage of mobile app badge images for the App Store and Play Store.

## Concept

Many websites display the "Get on Google Play" and "Download on the App Store"
badge images, advertising a mobile app download. This extension simplifies usage
by exposing the correct localized badge image via a YAML configuration file.

The images are included in SVG form with a tightly-cropped view box from:

- [App Store Brand Guidelines](https://developer.apple.com/app-store/marketing/guidelines/#section-badges)
- [Google Play Badge Generator](https://play.google.com/intl/en_us/badges/)

## Usage

### Grow setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-mobile-app-badges`
1. Run `grow install`.

### Usage via !g.static

1. Add the following section to `podspec.yaml`:

```
static_dirs:
- static_dir: '/extensions/grow_mobile_app_badges/images/'
  serve_at: '/{root}/static/images/badges/images/'  # Or similar.
```

2. Use in a content document:

```
app_store:
  label@: Download on the App Store
  url: https://example.com
  image: !g.yaml /extensions/grow_mobile_app_badges/static.yaml?app_store.image

play_store:
  label@: Download on the Play Store
  url: https://example.com
  image: !g.yaml /extensions/grow_mobile_app_badges/static.yaml?play_store.image
```

3. Use in a template:

```
<!-- App Store link. -->
<a href="{{doc.app_store.url}}" alt="{{doc.app_store.label}}"><img src="{{doc.app_store.image.url.path}}"></a>

<!-- Play Store link. -->
<a href="{{doc.play_store.url}}" alt="{{doc.play_store.label}}"><img src="{{doc.play_store.image.url.path}}"></a>
```

### Custom usage

1. Use in a content document:

```
app_store:
  label@: Download on the App Store
  url: https://example.com
  image: !g.yaml /extensions/grow_mobile_app_badges/pod_path.yaml?app_store.image

play_store:
  label@: Download on the Play Store
  url: https://example.com
  image: !g.yaml /extensions/grow_mobile_app_badges/pod_path.yaml?play_store.image
```

2. Use in a template (embeds SVG data directly):

```
<!-- App Store link. -->
<a href="{{doc.app_store.url}}" alt="{{doc.app_store.label}}">{% include doc.app_store.image %}</a>

<!-- Play Store link. -->
<a href="{{doc.play_store.url}}" alt="{{doc.play_store.label}}">{% include doc.play_store.image %}</a>
```
