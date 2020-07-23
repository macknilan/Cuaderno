





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-19e26a1cefb5f1e92203a9468134dbf46b5a5308aeeeee09c96b32fec8c8b044.css" integrity="sha256-GeJqHO+18ekiA6lGgTTb9GtaUwiu7u4JyWsy/sjIsEQ=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-a97f6b98170262f1be5dd5b84d3fb788f1bb65b269c11417026fe763d5eeb63b.css" integrity="sha256-qX9rmBcCYvG+XdW4TT+3iPG7ZbJpwRQXAm/nY9Xutjs=" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-1da8b9f73abeb68e6a54d0f514085224fe9e7325fd664eacacb38bebe10b9eab.css" integrity="sha256-Hai59zq+to5qVND1FAhSJP6ecyX9Zk6srLOL6+ELnqs=" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>gulp/API.md at master · gulpjs/gulp · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars0.githubusercontent.com/u/6200624?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="gulpjs/gulp" property="og:title" /><meta content="https://github.com/gulpjs/gulp" property="og:url" /><meta content="gulp - The streaming build system" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="9E88:64DB:406676:65E305:58BE1C5F" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="9E88:64DB:406676:65E305:58BE1C5F" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">



      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZGI4NWY4ZjM5ZDc1OWJiYzIwZDdhMGI0ODZhMzJlNGZmNzA3NjVkMWIyYWM5MzBlNDMwOTA2MTMyNzBlNGM4YXx7InJlbW90ZV9hZGRyZXNzIjoiMTg3LjE0NS4xMDguMzIiLCJyZXF1ZXN0X2lkIjoiOUU4ODo2NERCOjQwNjY3Njo2NUUzMDU6NThCRTFDNUYiLCJ0aW1lc3RhbXAiOjE0ODg4NTQxMTYsImhvc3QiOiJnaXRodWIuY29tIn0=">


  <meta name="html-safe-nonce" content="91fd0d787c323056bad009571c519433de6458b4">

  <meta http-equiv="x-pjax-version" content="6f7dd5e8045db8184cd083c6d969fed2">
  

    
  <meta name="description" content="gulp - The streaming build system">
  <meta name="go-import" content="github.com/gulpjs/gulp git https://github.com/gulpjs/gulp.git">

  <meta content="6200624" name="octolytics-dimension-user_id" /><meta content="gulpjs" name="octolytics-dimension-user_login" /><meta content="11167738" name="octolytics-dimension-repository_id" /><meta content="gulpjs/gulp" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="11167738" name="octolytics-dimension-repository_network_root_id" /><meta content="gulpjs/gulp" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/gulpjs/gulp/commits/master.atom" rel="alternate" title="Recent Commits to gulp:master" type="application/atom+xml">


    <link rel="canonical" href="https://github.com/gulpjs/gulp/blob/master/docs/API.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-out env-production linux page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



          <header class="site-header js-details-container Details" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>

    <button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
    </button>

    <div class="site-header-menu">
      <nav class="site-header-nav">
          <a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
            Features
</a>          <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
            Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing">
          Pricing
</a>      </nav>

      <div class="site-header-actions">
          <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/gulpjs/gulp/search" class="js-site-search-form" data-scoped-search-url="/gulpjs/gulp/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


          <a class="text-bold site-header-link" href="/login?return_to=%2Fgulpjs%2Fgulp%2Fblob%2Fmaster%2Fdocs%2FAPI.md" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
            <span class="text-gray">or</span>
            <a class="text-bold site-header-link" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
      <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
      <a href="/login?return_to=%2Fgulpjs%2Fgulp"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/gulpjs/gulp/watchers"
     aria-label="1157 users are watching this repository">
    1,157
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fgulpjs%2Fgulp"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/gulpjs/gulp/stargazers"
      aria-label="25428 users starred this repository">
      25,428
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fgulpjs%2Fgulp"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/gulpjs/gulp/network" class="social-count"
       aria-label="3621 users forked this repository">
      3,621
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/gulpjs" class="url fn" rel="author">gulpjs</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/gulpjs/gulp" data-pjax="#js-repo-pjax-container">gulp</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/gulpjs/gulp" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /gulpjs/gulp" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/gulpjs/gulp/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /gulpjs/gulp/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">23</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/gulpjs/gulp/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /gulpjs/gulp/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">3</span>
      <meta itemprop="position" content="3">
</a>  </span>

  <a href="/gulpjs/gulp/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /gulpjs/gulp/projects">
    <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
    Projects
    <span class="counter">0</span>
</a>


  <a href="/gulpjs/gulp/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /gulpjs/gulp/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/gulpjs/gulp/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /gulpjs/gulp/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/gulpjs/gulp/blob/62323fc55dd080a58ed030c5e9df176bdf551eae/docs/API.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:cef450b192817dfeca237ac354539dbb -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/gulpjs/gulp/blob/4.0/docs/API.md"
               data-name="4.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/gulpjs/gulp/blob/gfs-eval/docs/API.md"
               data-name="gfs-eval"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                gfs-eval
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/gulpjs/gulp/blob/master/docs/API.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/gulpjs/gulp/blob/new-docs/docs/API.md"
               data-name="new-docs"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                new-docs
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.9.1/docs/API.md"
              data-name="v3.9.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.9.1">
                v3.9.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.9.0/docs/API.md"
              data-name="v3.9.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.9.0">
                v3.9.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.11/docs/API.md"
              data-name="v3.8.11"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.11">
                v3.8.11
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.10/docs/API.md"
              data-name="v3.8.10"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.10">
                v3.8.10
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.9/docs/API.md"
              data-name="v3.8.9"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.9">
                v3.8.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.8/docs/API.md"
              data-name="v3.8.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.8">
                v3.8.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.7/docs/API.md"
              data-name="v3.8.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.7">
                v3.8.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.6/docs/API.md"
              data-name="v3.8.6"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.6">
                v3.8.6
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.5/docs/API.md"
              data-name="v3.8.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.5">
                v3.8.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.4/docs/API.md"
              data-name="v3.8.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.4">
                v3.8.4
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.3/docs/API.md"
              data-name="v3.8.3"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.3">
                v3.8.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/v3.8.1/docs/API.md"
              data-name="v3.8.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v3.8.1">
                v3.8.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/3.8/docs/API.md"
              data-name="3.8"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="3.8">
                3.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/3.7/docs/API.md"
              data-name="3.7"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="3.7">
                3.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/3.5/docs/API.md"
              data-name="3.5"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="3.5">
                3.5
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/gulpjs/gulp/tree/3.4/docs/API.md"
              data-name="3.4"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="3.4">
                3.4
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/gulpjs/gulp/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/gulpjs/gulp"><span>gulp</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/gulpjs/gulp/tree/master/docs"><span>docs</span></a></span><span class="separator">/</span><strong class="final-path">API.md</strong>
  </div>
</div>


  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/gulpjs/gulp/commit/5944c1b4d4c0a9dea804bc426b936aa742792cd4" data-pjax>
          5944c1b
        </a>
        <relative-time datetime="2016-05-13T18:50:29Z">May 13, 2016</relative-time>
      </span>
      <div>
        <img alt="@makoConstruct" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/346569?v=3&amp;s=40" width="20" />
        <a href="/makoConstruct" class="user-mention" rel="contributor">makoConstruct</a>
          <a href="/gulpjs/gulp/commit/5944c1b4d4c0a9dea804bc426b936aa742792cd4" class="message" data-pjax="true" title="correct gulp.task signature (#1653)

* correct gulp.task signature

`gulp.task(name [, deps, fn])` means that only `gulp.task(name, deps, fn)` and `gulp.task(name)` are allowed, which is apparently not the case and it's a bit confusing. The correct notation, `gulp.task(name [, deps] [, fn])`, also permits for `gulp.task(name, deps)`, and `gulp.task(name, fn)`.

* fixed indexing">correct gulp.task signature (</a><a href="https://github.com/gulpjs/gulp/pull/1653" class="issue-link js-issue-link" data-url="https://github.com/gulpjs/gulp/issues/1653" data-id="154381930" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#1653</a><a href="/gulpjs/gulp/commit/5944c1b4d4c0a9dea804bc426b936aa742792cd4" class="message" data-pjax="true" title="correct gulp.task signature (#1653)

* correct gulp.task signature

`gulp.task(name [, deps, fn])` means that only `gulp.task(name, deps, fn)` and `gulp.task(name)` are allowed, which is apparently not the case and it's a bit confusing. The correct notation, `gulp.task(name [, deps] [, fn])`, also permits for `gulp.task(name, deps)`, and `gulp.task(name, fn)`.

* fixed indexing">)</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>28</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="contra" href="/gulpjs/gulp/commits/master/docs/API.md?author=contra"><img alt="@contra" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/425716?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sanfords" href="/gulpjs/gulp/commits/master/docs/API.md?author=sanfords"><img alt="@sanfords" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/1291701?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="robrich" href="/gulpjs/gulp/commits/master/docs/API.md?author=robrich"><img alt="@robrich" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/664956?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="breyed" href="/gulpjs/gulp/commits/master/docs/API.md?author=breyed"><img alt="@breyed" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/1299073?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mariuszskon" href="/gulpjs/gulp/commits/master/docs/API.md?author=mariuszskon"><img alt="@mariuszskon" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/13817113?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="t3chnoboy" href="/gulpjs/gulp/commits/master/docs/API.md?author=t3chnoboy"><img alt="@t3chnoboy" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/2552790?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="xixixao" href="/gulpjs/gulp/commits/master/docs/API.md?author=xixixao"><img alt="@xixixao" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/1473433?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="terinjokes" href="/gulpjs/gulp/commits/master/docs/API.md?author=terinjokes"><img alt="@terinjokes" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/273509?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="stevemao" href="/gulpjs/gulp/commits/master/docs/API.md?author=stevemao"><img alt="@stevemao" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/6316590?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="ceclinux" href="/gulpjs/gulp/commits/master/docs/API.md?author=ceclinux"><img alt="@ceclinux" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/2628211?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sindresorhus" href="/gulpjs/gulp/commits/master/docs/API.md?author=sindresorhus"><img alt="@sindresorhus" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/170270?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="erquhart" href="/gulpjs/gulp/commits/master/docs/API.md?author=erquhart"><img alt="@erquhart" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/2112202?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="BusyRich" href="/gulpjs/gulp/commits/master/docs/API.md?author=BusyRich"><img alt="@BusyRich" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/940411?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="pkozlowski-opensource" href="/gulpjs/gulp/commits/master/docs/API.md?author=pkozlowski-opensource"><img alt="@pkozlowski-opensource" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/973550?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="briandipalma" href="/gulpjs/gulp/commits/master/docs/API.md?author=briandipalma"><img alt="@briandipalma" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/1597820?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="stevelacy" href="/gulpjs/gulp/commits/master/docs/API.md?author=stevelacy"><img alt="@stevelacy" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/5648999?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="matthieuprat" href="/gulpjs/gulp/commits/master/docs/API.md?author=matthieuprat"><img alt="@matthieuprat" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/890117?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="MarkLeMerise" href="/gulpjs/gulp/commits/master/docs/API.md?author=MarkLeMerise"><img alt="@MarkLeMerise" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/573634?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="makoConstruct" href="/gulpjs/gulp/commits/master/docs/API.md?author=makoConstruct"><img alt="@makoConstruct" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/346569?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kevdez" href="/gulpjs/gulp/commits/master/docs/API.md?author=kevdez"><img alt="@kevdez" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/6848941?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kdex" href="/gulpjs/gulp/commits/master/docs/API.md?author=kdex"><img alt="@kdex" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/4442505?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jgillich" href="/gulpjs/gulp/commits/master/docs/API.md?author=jgillich"><img alt="@jgillich" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/347965?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="RnbWd" href="/gulpjs/gulp/commits/master/docs/API.md?author=RnbWd"><img alt="@RnbWd" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/5370305?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tohashi" href="/gulpjs/gulp/commits/master/docs/API.md?author=tohashi"><img alt="@tohashi" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1400168?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="demisx" href="/gulpjs/gulp/commits/master/docs/API.md?author=demisx"><img alt="@demisx" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/4452412?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="barneycarroll" href="/gulpjs/gulp/commits/master/docs/API.md?author=barneycarroll"><img alt="@barneycarroll" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/83627?v=3&amp;s=40" width="20" /> </a>

    <button type="button" data-facebox="#blob_contributors_box" class="btn-link others-text">and others</button>

    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@contra" height="24" src="https://avatars3.githubusercontent.com/u/425716?v=3&amp;s=48" width="24" />
            <a href="/contra">contra</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sanfords" height="24" src="https://avatars1.githubusercontent.com/u/1291701?v=3&amp;s=48" width="24" />
            <a href="/sanfords">sanfords</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@robrich" height="24" src="https://avatars0.githubusercontent.com/u/664956?v=3&amp;s=48" width="24" />
            <a href="/robrich">robrich</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@breyed" height="24" src="https://avatars1.githubusercontent.com/u/1299073?v=3&amp;s=48" width="24" />
            <a href="/breyed">breyed</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mariuszskon" height="24" src="https://avatars0.githubusercontent.com/u/13817113?v=3&amp;s=48" width="24" />
            <a href="/mariuszskon">mariuszskon</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@t3chnoboy" height="24" src="https://avatars1.githubusercontent.com/u/2552790?v=3&amp;s=48" width="24" />
            <a href="/t3chnoboy">t3chnoboy</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@xixixao" height="24" src="https://avatars0.githubusercontent.com/u/1473433?v=3&amp;s=48" width="24" />
            <a href="/xixixao">xixixao</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@terinjokes" height="24" src="https://avatars3.githubusercontent.com/u/273509?v=3&amp;s=48" width="24" />
            <a href="/terinjokes">terinjokes</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@stevemao" height="24" src="https://avatars2.githubusercontent.com/u/6316590?v=3&amp;s=48" width="24" />
            <a href="/stevemao">stevemao</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@ceclinux" height="24" src="https://avatars1.githubusercontent.com/u/2628211?v=3&amp;s=48" width="24" />
            <a href="/ceclinux">ceclinux</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sindresorhus" height="24" src="https://avatars2.githubusercontent.com/u/170270?v=3&amp;s=48" width="24" />
            <a href="/sindresorhus">sindresorhus</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@erquhart" height="24" src="https://avatars1.githubusercontent.com/u/2112202?v=3&amp;s=48" width="24" />
            <a href="/erquhart">erquhart</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@BusyRich" height="24" src="https://avatars3.githubusercontent.com/u/940411?v=3&amp;s=48" width="24" />
            <a href="/BusyRich">BusyRich</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@pkozlowski-opensource" height="24" src="https://avatars1.githubusercontent.com/u/973550?v=3&amp;s=48" width="24" />
            <a href="/pkozlowski-opensource">pkozlowski-opensource</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@briandipalma" height="24" src="https://avatars0.githubusercontent.com/u/1597820?v=3&amp;s=48" width="24" />
            <a href="/briandipalma">briandipalma</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@stevelacy" height="24" src="https://avatars1.githubusercontent.com/u/5648999?v=3&amp;s=48" width="24" />
            <a href="/stevelacy">stevelacy</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@matthieuprat" height="24" src="https://avatars3.githubusercontent.com/u/890117?v=3&amp;s=48" width="24" />
            <a href="/matthieuprat">matthieuprat</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@MarkLeMerise" height="24" src="https://avatars0.githubusercontent.com/u/573634?v=3&amp;s=48" width="24" />
            <a href="/MarkLeMerise">MarkLeMerise</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@makoConstruct" height="24" src="https://avatars0.githubusercontent.com/u/346569?v=3&amp;s=48" width="24" />
            <a href="/makoConstruct">makoConstruct</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@kevdez" height="24" src="https://avatars1.githubusercontent.com/u/6848941?v=3&amp;s=48" width="24" />
            <a href="/kevdez">kevdez</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@kdex" height="24" src="https://avatars1.githubusercontent.com/u/4442505?v=3&amp;s=48" width="24" />
            <a href="/kdex">kdex</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@jgillich" height="24" src="https://avatars2.githubusercontent.com/u/347965?v=3&amp;s=48" width="24" />
            <a href="/jgillich">jgillich</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@RnbWd" height="24" src="https://avatars2.githubusercontent.com/u/5370305?v=3&amp;s=48" width="24" />
            <a href="/RnbWd">RnbWd</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@tohashi" height="24" src="https://avatars3.githubusercontent.com/u/1400168?v=3&amp;s=48" width="24" />
            <a href="/tohashi">tohashi</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@demisx" height="24" src="https://avatars1.githubusercontent.com/u/4452412?v=3&amp;s=48" width="24" />
            <a href="/demisx">demisx</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@barneycarroll" height="24" src="https://avatars0.githubusercontent.com/u/83627?v=3&amp;s=48" width="24" />
            <a href="/barneycarroll">barneycarroll</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@AndrewSouthpaw" height="24" src="https://avatars0.githubusercontent.com/u/5187404?v=3&amp;s=48" width="24" />
            <a href="/AndrewSouthpaw">AndrewSouthpaw</a>
          </li>
      </ul>
    </div>
  </div>


<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/gulpjs/gulp/raw/master/docs/API.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/gulpjs/gulp/blame/master/docs/API.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/gulpjs/gulp/commits/master/docs/API.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      324 lines (226 sloc)
      <span class="file-info-divider"></span>
    8.59 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h2><a id="user-content-gulp-api-docs" class="anchor" href="#gulp-api-docs" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp API docs</h2>

<p>Jump to:
  <a href="#gulpsrcglobs-options">gulp.src</a> |
  <a href="#gulpdestpath-options">gulp.dest</a> |
  <a href="#gulptaskname--deps--fn">gulp.task</a> |
  <a href="#gulpwatchglob--opts-tasks-or-gulpwatchglob--opts-cb">gulp.watch</a></p>

<h3><a id="user-content-gulpsrcglobs-options" class="anchor" href="#gulpsrcglobs-options" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.src(globs[, options])</h3>

<p>Emits files matching provided glob or an array of globs.
Returns a <a href="http://nodejs.org/api/stream.html">stream</a> of <a href="https://github.com/gulpjs/vinyl-fs">Vinyl files</a>
that can be <a href="http://nodejs.org/api/stream.html#stream_readable_pipe_destination_options">piped</a>
to plugins.</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-s"><span class="pl-pds">'</span>client/templates/*.jade<span class="pl-pds">'</span></span>)
  .<span class="pl-en">pipe</span>(<span class="pl-en">jade</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>build/minified_templates<span class="pl-pds">'</span></span>));</pre></div>

<h4><a id="user-content-globs" class="anchor" href="#globs" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>globs</h4>

<p>Type: <code>String</code> or <code>Array</code></p>

<p>Glob or array of globs to read. Globs use <a href="https://github.com/isaacs/node-glob">node-glob syntax</a> except that negation is fully supported.</p>

<p>A glob that begins with <code>!</code> excludes matching files from the glob results up to that point. For example, consider this directory structure:</p>

<pre><code>client/
  a.js
  bob.js
  bad.js
</code></pre>

<p>The following expression matches <code>a.js</code> and <code>bad.js</code>:</p>

<pre><code>gulp.src(['client/*.js', '!client/b*.js', 'client/bad.js'])
</code></pre>

<h4><a id="user-content-options" class="anchor" href="#options" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options</h4>

<p>Type: <code>Object</code></p>

<p>Options to pass to <a href="https://github.com/isaacs/node-glob">node-glob</a> through <a href="https://github.com/gulpjs/glob-stream">glob-stream</a>.</p>

<p>gulp supports all <a href="https://github.com/isaacs/node-glob#options">options supported by node-glob</a> and <a href="https://github.com/gulpjs/glob-stream">glob-stream</a> except <code>ignore</code> and adds the following options.</p>

<h5><a id="user-content-optionsbuffer" class="anchor" href="#optionsbuffer" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options.buffer</h5>

<p>Type: <code>Boolean</code>
Default: <code>true</code></p>

<p>Setting this to <code>false</code> will return <code>file.contents</code> as a stream and not buffer files. This is useful when working with large files. <strong>Note:</strong> Plugins might not implement support for streams.</p>

<h5><a id="user-content-optionsread" class="anchor" href="#optionsread" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options.read</h5>

<p>Type: <code>Boolean</code>
Default: <code>true</code></p>

<p>Setting this to <code>false</code> will return <code>file.contents</code> as null and not read the file at all.</p>

<h5><a id="user-content-optionsbase" class="anchor" href="#optionsbase" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options.base</h5>

<p>Type: <code>String</code>
Default: everything before a glob starts (see <a href="https://github.com/wearefractal/glob2base">glob2base</a>)</p>

<p>E.g., consider <code>somefile.js</code> in <code>client/js/somedir</code>:</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-s"><span class="pl-pds">'</span>client/js/**/*.js<span class="pl-pds">'</span></span>) <span class="pl-c"><span class="pl-c">//</span> Matches 'client/js/somedir/somefile.js' and resolves `base` to `client/js/`</span>
  .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>build<span class="pl-pds">'</span></span>));  <span class="pl-c"><span class="pl-c">//</span> Writes 'build/somedir/somefile.js'</span>

<span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-s"><span class="pl-pds">'</span>client/js/**/*.js<span class="pl-pds">'</span></span>, { base<span class="pl-k">:</span> <span class="pl-s"><span class="pl-pds">'</span>client<span class="pl-pds">'</span></span> })
  .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>build<span class="pl-pds">'</span></span>));  <span class="pl-c"><span class="pl-c">//</span> Writes 'build/js/somedir/somefile.js'</span></pre></div>

<h3><a id="user-content-gulpdestpath-options" class="anchor" href="#gulpdestpath-options" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.dest(path[, options])</h3>

<p>Can be piped to and it will write files. Re-emits all data passed to it so you can pipe to multiple folders.  Folders that don't exist will be created.</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-s"><span class="pl-pds">'</span>./client/templates/*.jade<span class="pl-pds">'</span></span>)
  .<span class="pl-en">pipe</span>(<span class="pl-en">jade</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>./build/templates<span class="pl-pds">'</span></span>))
  .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>./build/minified_templates<span class="pl-pds">'</span></span>));</pre></div>

<p>The write path is calculated by appending the file relative path to the given
destination directory. In turn, relative paths are calculated against the file base.
See <code>gulp.src</code> above for more info.</p>

<h4><a id="user-content-path" class="anchor" href="#path" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>path</h4>

<p>Type: <code>String</code> or <code>Function</code></p>

<p>The path (output folder) to write files to. Or a function that returns it, the function will be provided a <a href="https://github.com/gulpjs/vinyl">vinyl File instance</a>.</p>

<h4><a id="user-content-options-1" class="anchor" href="#options-1" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options</h4>

<p>Type: <code>Object</code></p>

<h5><a id="user-content-optionscwd" class="anchor" href="#optionscwd" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options.cwd</h5>

<p>Type: <code>String</code>
Default: <code>process.cwd()</code></p>

<p><code>cwd</code> for the output folder, only has an effect if provided output folder is relative.</p>

<h5><a id="user-content-optionsmode" class="anchor" href="#optionsmode" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>options.mode</h5>

<p>Type: <code>String</code>
Default: <code>0777</code></p>

<p>Octal permission string specifying mode for any folders that need to be created for output folder.</p>

<h3><a id="user-content-gulptaskname--deps--fn" class="anchor" href="#gulptaskname--deps--fn" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.task(name [, deps] [, fn])</h3>

<p>Define a task using <a href="https://github.com/robrich/orchestrator">Orchestrator</a>.</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>somename<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-c"><span class="pl-c">//</span> Do stuff</span>
});</pre></div>

<h4><a id="user-content-name" class="anchor" href="#name" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>name</h4>

<p>Type: <code>String</code></p>

<p>The name of the task. Tasks that you want to run from the command line should not have spaces in them.</p>

<h4><a id="user-content-deps" class="anchor" href="#deps" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>deps</h4>

<p>Type: <code>Array</code></p>

<p>An array of tasks to be executed and completed before your task will run.</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>mytask<span class="pl-pds">'</span></span>, [<span class="pl-s"><span class="pl-pds">'</span>array<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>of<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>task<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>names<span class="pl-pds">'</span></span>], <span class="pl-k">function</span>() {
  <span class="pl-c"><span class="pl-c">//</span> Do stuff</span>
});</pre></div>

<p><strong>Note:</strong> Are your tasks running before the dependencies are complete?  Make sure your dependency tasks are correctly using the async run hints: take in a callback or return a promise or event stream.</p>

<p>You can also omit the function if you only want to run a bundle of dependency tasks:</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>build<span class="pl-pds">'</span></span>, [<span class="pl-s"><span class="pl-pds">'</span>array<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>of<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>task<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>names<span class="pl-pds">'</span></span>]);</pre></div>

<p><strong>Note:</strong> The tasks will run in parallel (all at once), so don't assume that the tasks will start/finish in order.</p>

<h4><a id="user-content-fn" class="anchor" href="#fn" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>fn</h4>

<p>Type: <code>Function</code></p>

<p>The function performs the task's main operations. Generally this takes the form of:</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>buildStuff<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-c"><span class="pl-c">//</span> Do something that "builds stuff"</span>
  <span class="pl-k">var</span> stream <span class="pl-k">=</span> <span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-c"><span class="pl-c">/*</span>some source path<span class="pl-c">*/</span></span>)
  .<span class="pl-en">pipe</span>(<span class="pl-en">somePlugin</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-en">someOtherPlugin</span>())
  .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-c"><span class="pl-c">/*</span>some destination<span class="pl-c">*/</span></span>));

  <span class="pl-k">return</span> stream;
  });</pre></div>

<h4><a id="user-content-async-task-support" class="anchor" href="#async-task-support" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Async task support</h4>

<p>Tasks can be made asynchronous if its <code>fn</code> does one of the following:</p>

<h5><a id="user-content-accept-a-callback" class="anchor" href="#accept-a-callback" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Accept a callback</h5>

<div class="highlight highlight-source-js"><pre><span class="pl-c"><span class="pl-c">//</span> run a command in a shell</span>
<span class="pl-k">var</span> exec <span class="pl-k">=</span> <span class="pl-c1">require</span>(<span class="pl-s"><span class="pl-pds">'</span>child_process<span class="pl-pds">'</span></span>).<span class="pl-smi">exec</span>;
<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>jekyll<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-smi">cb</span>) {
  <span class="pl-c"><span class="pl-c">//</span> build Jekyll</span>
  <span class="pl-en">exec</span>(<span class="pl-s"><span class="pl-pds">'</span>jekyll build<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-smi">err</span>) {
    <span class="pl-k">if</span> (err) <span class="pl-k">return</span> <span class="pl-en">cb</span>(err); <span class="pl-c"><span class="pl-c">//</span> return error</span>
    <span class="pl-en">cb</span>(); <span class="pl-c"><span class="pl-c">//</span> finished task</span>
  });
});

<span class="pl-c"><span class="pl-c">//</span> use an async result in a pipe</span>
<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>somename<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-smi">cb</span>) {
  <span class="pl-en">getFilesAsync</span>(<span class="pl-k">function</span>(<span class="pl-smi">err</span>, <span class="pl-smi">res</span>) {
    <span class="pl-k">if</span> (err) <span class="pl-k">return</span> <span class="pl-en">cb</span>(err);
    <span class="pl-k">var</span> stream <span class="pl-k">=</span> <span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(res)
      .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
      .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>build<span class="pl-pds">'</span></span>))
      .<span class="pl-en">on</span>(<span class="pl-s"><span class="pl-pds">'</span>end<span class="pl-pds">'</span></span>, cb);
  });
});</pre></div>

<h5><a id="user-content-return-a-stream" class="anchor" href="#return-a-stream" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Return a stream</h5>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>somename<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-k">var</span> stream <span class="pl-k">=</span> <span class="pl-smi">gulp</span>.<span class="pl-en">src</span>(<span class="pl-s"><span class="pl-pds">'</span>client/**/*.js<span class="pl-pds">'</span></span>)
    .<span class="pl-en">pipe</span>(<span class="pl-en">minify</span>())
    .<span class="pl-en">pipe</span>(<span class="pl-smi">gulp</span>.<span class="pl-en">dest</span>(<span class="pl-s"><span class="pl-pds">'</span>build<span class="pl-pds">'</span></span>));
  <span class="pl-k">return</span> stream;
});</pre></div>

<h5><a id="user-content-return-a-promise" class="anchor" href="#return-a-promise" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Return a promise</h5>

<div class="highlight highlight-source-js"><pre><span class="pl-k">var</span> <span class="pl-c1">Q</span> <span class="pl-k">=</span> <span class="pl-c1">require</span>(<span class="pl-s"><span class="pl-pds">'</span>q<span class="pl-pds">'</span></span>);

<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>somename<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>() {
  <span class="pl-k">var</span> deferred <span class="pl-k">=</span> <span class="pl-c1">Q</span>.<span class="pl-c1">defer</span>();

  <span class="pl-c"><span class="pl-c">//</span> do async stuff</span>
  <span class="pl-c1">setTimeout</span>(<span class="pl-k">function</span>() {
    <span class="pl-smi">deferred</span>.<span class="pl-en">resolve</span>();
  }, <span class="pl-c1">1</span>);

  <span class="pl-k">return</span> <span class="pl-smi">deferred</span>.<span class="pl-smi">promise</span>;
});</pre></div>

<p><strong>Note:</strong> By default, tasks run with maximum concurrency -- e.g. it launches all the tasks at once and waits for nothing. If you want to create a series where tasks run in a particular order, you need to do two things:</p>

<ul>
<li>give it a hint to tell it when the task is done,</li>
<li>and give it a hint that a task depends on completion of another.</li>
</ul>

<p>For these examples, let's presume you have two tasks, "one" and "two" that you specifically want to run in this order:</p>

<ol>
<li><p>In task "one" you add a hint to tell it when the task is done.  Either take in a callback and call it when you're
done or return a promise or stream that the engine should wait to resolve or end respectively.</p></li>
<li><p>In task "two" you add a hint telling the engine that it depends on completion of the first task.</p></li>
</ol>

<p>So this example would look like this:</p>

<div class="highlight highlight-source-js"><pre><span class="pl-k">var</span> gulp <span class="pl-k">=</span> <span class="pl-c1">require</span>(<span class="pl-s"><span class="pl-pds">'</span>gulp<span class="pl-pds">'</span></span>);

<span class="pl-c"><span class="pl-c">//</span> takes in a callback so the engine knows when it'll be done</span>
<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>one<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-smi">cb</span>) {
    <span class="pl-c"><span class="pl-c">//</span> do stuff -- async or otherwise</span>
    <span class="pl-en">cb</span>(err); <span class="pl-c"><span class="pl-c">//</span> if err is not null and not undefined, the run will stop, and note that it failed</span>
});

<span class="pl-c"><span class="pl-c">//</span> identifies a dependent task must be complete before this one begins</span>
<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>two<span class="pl-pds">'</span></span>, [<span class="pl-s"><span class="pl-pds">'</span>one<span class="pl-pds">'</span></span>], <span class="pl-k">function</span>() {
    <span class="pl-c"><span class="pl-c">//</span> task 'one' is done now</span>
});

<span class="pl-smi">gulp</span>.<span class="pl-en">task</span>(<span class="pl-s"><span class="pl-pds">'</span>default<span class="pl-pds">'</span></span>, [<span class="pl-s"><span class="pl-pds">'</span>one<span class="pl-pds">'</span></span>, <span class="pl-s"><span class="pl-pds">'</span>two<span class="pl-pds">'</span></span>]);</pre></div>

<h3><a id="user-content-gulpwatchglob--opts-tasks-or-gulpwatchglob--opts-cb" class="anchor" href="#gulpwatchglob--opts-tasks-or-gulpwatchglob--opts-cb" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.watch(glob [, opts], tasks) or gulp.watch(glob [, opts, cb])</h3>

<p>Watch files and do something when a file changes. This always returns an EventEmitter that emits <code>change</code> events.</p>

<h3><a id="user-content-gulpwatchglob-opts-tasks" class="anchor" href="#gulpwatchglob-opts-tasks" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.watch(glob[, opts], tasks)</h3>

<h4><a id="user-content-glob" class="anchor" href="#glob" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>glob</h4>

<p>Type: <code>String</code> or <code>Array</code></p>

<p>A single glob or array of globs that indicate which files to watch for changes.</p>

<h4><a id="user-content-opts" class="anchor" href="#opts" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>opts</h4>

<p>Type: <code>Object</code></p>

<p>Options, that are passed to <a href="https://github.com/shama/gaze"><code>gaze</code></a>.</p>

<h4><a id="user-content-tasks" class="anchor" href="#tasks" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>tasks</h4>

<p>Type: <code>Array</code></p>

<p>Names of task(s) to run when a file changes, added with <code>gulp.task()</code></p>

<div class="highlight highlight-source-js"><pre><span class="pl-k">var</span> watcher <span class="pl-k">=</span> <span class="pl-smi">gulp</span>.<span class="pl-c1">watch</span>(<span class="pl-s"><span class="pl-pds">'</span>js/**/*.js<span class="pl-pds">'</span></span>, [<span class="pl-s"><span class="pl-pds">'</span>uglify<span class="pl-pds">'</span></span>,<span class="pl-s"><span class="pl-pds">'</span>reload<span class="pl-pds">'</span></span>]);
<span class="pl-smi">watcher</span>.<span class="pl-en">on</span>(<span class="pl-s"><span class="pl-pds">'</span>change<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-c1">event</span>) {
  <span class="pl-en">console</span>.<span class="pl-c1">log</span>(<span class="pl-s"><span class="pl-pds">'</span>File <span class="pl-pds">'</span></span> <span class="pl-k">+</span> <span class="pl-c1">event</span>.<span class="pl-smi">path</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">'</span> was <span class="pl-pds">'</span></span> <span class="pl-k">+</span> <span class="pl-c1">event</span>.<span class="pl-c1">type</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">'</span>, running tasks...<span class="pl-pds">'</span></span>);
});</pre></div>

<h3><a id="user-content-gulpwatchglob-opts-cb" class="anchor" href="#gulpwatchglob-opts-cb" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gulp.watch(glob[, opts, cb])</h3>

<h4><a id="user-content-glob-1" class="anchor" href="#glob-1" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>glob</h4>

<p>Type: <code>String</code> or <code>Array</code></p>

<p>A single glob or array of globs that indicate which files to watch for changes.</p>

<h4><a id="user-content-opts-1" class="anchor" href="#opts-1" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>opts</h4>

<p>Type: <code>Object</code></p>

<p>Options, that are passed to <a href="https://github.com/shama/gaze"><code>gaze</code></a>.</p>

<h4><a id="user-content-cbevent" class="anchor" href="#cbevent" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>cb(event)</h4>

<p>Type: <code>Function</code></p>

<p>Callback to be called on each change.</p>

<div class="highlight highlight-source-js"><pre><span class="pl-smi">gulp</span>.<span class="pl-c1">watch</span>(<span class="pl-s"><span class="pl-pds">'</span>js/**/*.js<span class="pl-pds">'</span></span>, <span class="pl-k">function</span>(<span class="pl-c1">event</span>) {
  <span class="pl-en">console</span>.<span class="pl-c1">log</span>(<span class="pl-s"><span class="pl-pds">'</span>File <span class="pl-pds">'</span></span> <span class="pl-k">+</span> <span class="pl-c1">event</span>.<span class="pl-smi">path</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">'</span> was <span class="pl-pds">'</span></span> <span class="pl-k">+</span> <span class="pl-c1">event</span>.<span class="pl-c1">type</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">'</span>, running tasks...<span class="pl-pds">'</span></span>);
});</pre></div>

<p>The callback will be passed an object, <code>event</code>, that describes the change:</p>

<h5><a id="user-content-eventtype" class="anchor" href="#eventtype" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>event.type</h5>

<p>Type: <code>String</code></p>

<p>The type of change that occurred, either <code>added</code>, <code>changed</code>, <code>deleted</code> or <code>renamed</code>.</p>

<h5><a id="user-content-eventpath" class="anchor" href="#eventpath" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>event.path</h5>

<p>Type: <code>String</code></p>

<p>The path to the file that triggered the event.</p>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>


    </div>
  </div>

  </div>

      <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.13467s from github-fe146-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  

  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha256-heRlCfWR3OdZXbrJe84Z7qKV1BIgf6n43Vv98CCGlh4=" src="https://assets-cdn.github.com/assets/frameworks-85e46509f591dce7595dbac97bce19eea295d412207fa9f8dd5bfdf02086961e.js"></script>
    <script async="async" crossorigin="anonymous" integrity="sha256-ryLKldCeCTfJ2efyNRPErDp3+95s6raTSGZ7kotVpnw=" src="https://assets-cdn.github.com/assets/github-af22ca95d09e0937c9d9e7f23513c4ac3a77fbde6ceab69348667b928b55a67c.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

