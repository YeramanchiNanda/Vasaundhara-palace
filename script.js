document.addEventListener('DOMContentLoaded', () => {
    
    // --- Premium Preloader Fade (Guaranteed Execution) ---
    const removePreloader = () => {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            preloader.style.opacity = '0';
            preloader.style.visibility = 'hidden';
            setTimeout(() => { preloader.style.display = 'none'; }, 800);
        }
    };
    
    // Attempt standard removal, but guarantee forced fade out after 1.5 seconds.
    window.addEventListener('load', removePreloader);
    setTimeout(removePreloader, 1500);
    // 1. Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    mobileBtn.addEventListener('click', () => {
        // Simple toggle for now (could be expanded into a fullscreen menu)
        navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.width = '100%';
        navLinks.style.background = 'rgba(10,10,10,0.95)';
        navLinks.style.padding = '2rem';
        navLinks.style.borderBottom = '1px solid rgba(212,175,55,0.3)';
    });

    // 2. Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                // Adjust for navbar height
                const navHeight = navbar.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                if (window.innerWidth <= 768 && navLinks.style.display === 'flex') {
                    navLinks.style.display = 'none';
                }
            }
        });
    });

    // 4. Parallax Effect for Hero section
    const heroBg = document.querySelector('.parallax-bg');
    window.addEventListener('scroll', () => {
        const scroll = window.scrollY;
        if (scroll < window.innerHeight && heroBg) {
            // Slow pan down on scroll
            heroBg.style.transform = `scale(1.1) translateY(${scroll * 0.4}px)`;
        }
    });

    // 5. Cinematic Video Playlist Logic
    const videoElement = document.getElementById('hero-playlist-video');
    if (videoElement) {
        // Force remove loop attribute in case your browser is holding an older cached version of the HTML
        videoElement.removeAttribute('loop');
        
        // The list of sequentially named video files the website will look for
        const playlist = [
            'assets/vasundhara-hero.mp4',
            'assets/vasundhara-hero2.mp4',
            'assets/vasundhara-hero3.mp4',
            'assets/vasundhara-hero4.mp4',
            'assets/vasundhara-hero5.mp4'
        ];
        let currentVideoIndex = 0;

        // When a video finishes, play the next one
        videoElement.addEventListener('ended', () => {
            currentVideoIndex++;
            if (currentVideoIndex >= playlist.length) {
                currentVideoIndex = 0; 
            }
            videoElement.src = playlist[currentVideoIndex];
            videoElement.load();
            
            // Small internal delay to ensure the browser has loaded the new file source
            setTimeout(() => {
                const playPromise = videoElement.play();
                if (playPromise !== undefined) {
                    playPromise.catch(e => {
                        if (currentVideoIndex !== 0) {
                            currentVideoIndex = 0;
                            videoElement.src = playlist[0];
                            videoElement.load();
                            videoElement.play();
                        }
                    });
                }
            }, 50);
        });

        // If a video file is missing (e.g., you only uploaded 2 out of 5), 
        // the browser gracefully catches the error and loops back to the first video automatically
        videoElement.addEventListener('error', () => {
            if (currentVideoIndex !== 0) {
                currentVideoIndex = 0;
                videoElement.src = playlist[0];
                videoElement.load();
                videoElement.play();
            }
        }, true);
    }

    // 6. Scroll Reveal Animations utilizing IntersectionObserver
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-right');
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }
            entry.target.classList.add('active');
            observer.unobserve(entry.target); // Trigger only once
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // 6. Split-View Menu Intersection Observer (Scrollspy)
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    const menuGroups = document.querySelectorAll('.menu-category-group');
    
    // Smooth scrolling for sidebar links
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetGroup = document.querySelector(targetId);
            
            if (targetGroup) {
                // Ensure manual scroll triggers smooth scroll and respects sticky headers
                const navHeight = document.querySelector('.navbar').offsetHeight;
                const mobileNavHeight = window.innerWidth <= 992 ? 80 : 0; // extra offset for mobile sticky bar
                const targetPosition = targetGroup.getBoundingClientRect().top + window.pageYOffset - navHeight - mobileNavHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Observer to update active sidebar link based on scroll position
    const menuObserverOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
    };

    const menuObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const currentId = entry.target.getAttribute('id');
                
                sidebarLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${currentId}`) {
                        link.classList.add('active');
                        // Scroll the sidebar link into view horizontally on mobile
                        if (window.innerWidth <= 992) {
                            link.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                        }
                    }
                });
            }
        });
    }, menuObserverOptions);

    menuGroups.forEach(group => {
        menuObserver.observe(group);
    });

    // --- Museum Gallery Auto-Scroll Engine ---
    const galleryGrid = document.querySelector('.museum-grid');
    if (galleryGrid) {
        let isHovered = false;
        let scrollInterval;
        
        const startScroll = () => {
            scrollInterval = setInterval(() => {
                if (!isHovered) {
                    galleryGrid.scrollLeft += 1.5; // Smooth incremental speed
                    
                    // Loop back to start smoothly when reaching the end
                    if (galleryGrid.scrollLeft >= (galleryGrid.scrollWidth - galleryGrid.clientWidth - 2)) {
                        galleryGrid.scrollLeft = 0;
                    }
                }
            }, 25); // ~40 FPS for smooth pacing
        };

        // Pause auto-scroll on interactions
        galleryGrid.addEventListener('mouseenter', () => isHovered = true);
        galleryGrid.addEventListener('mouseleave', () => isHovered = false);
        galleryGrid.addEventListener('touchstart', () => isHovered = true, { passive: true });
        galleryGrid.addEventListener('touchend', () => {
            // Add a slight delay before resuming scroll after touch
            setTimeout(() => { isHovered = false; }, 1000); 
        });

        startScroll();
    }

    // --- Cinematic Widescreen Expansion (Option 1) ---
    const expansionSection = document.querySelector('.cinematic-expansion-section');
    const expansionWindow = document.getElementById('expansionWindow');
    const expansionContent = document.querySelector('.expansion-content');
    
    if (expansionSection && expansionWindow) {
        window.addEventListener('scroll', () => {
            const rect = expansionSection.getBoundingClientRect();
            // rect.top goes from 0 (when sections starts) to negative (when scrolling)
            
            // The amount of scroll track (200vh - 100vh = 100vh distance)
            const scrollDistance = window.innerHeight; 
            
            // Calculate progress between 0 and 1
            let progress = -rect.top / scrollDistance;
            progress = Math.max(0, Math.min(1, progress));
            
            // Map progress to width (60% to 100%) and height (40vh to 100vh)
            // Mobile adjustments check
            const isMobile = window.innerWidth <= 992;
            const startWidth = isMobile ? 85 : 60;
            const startHeight = isMobile ? 35 : 40;
            
            const currentWidth = startWidth + ((100 - startWidth) * progress);
            const currentHeight = startHeight + ((100 - startHeight) * progress);
            
            // Map progress to border-radius (24px to 0px)
            const currentRadius = 24 * (1 - progress);
            
            expansionWindow.style.width = `${currentWidth}vw`;
            expansionWindow.style.height = `${currentHeight}vh`;
            expansionWindow.style.borderRadius = `${currentRadius}px`;
            
            // Pop text at full expansion
            if (progress > 0.85) {
                expansionContent.classList.add('active');
            } else {
                expansionContent.classList.remove('active');
            }
        });
    }
});
