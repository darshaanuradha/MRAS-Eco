/* ============================================
   MRAS Eco — Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

    // ═══════════════════════════════════════
    // SIDEBAR TOGGLE (Mobile)
    // ═══════════════════════════════════════

    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    const sidebarOpenBtn = document.getElementById('sidebar-open-btn');
    const sidebarCloseBtn = document.getElementById('sidebar-close-btn');

    function openSidebar() {
        if (!sidebar) return;
        sidebar.classList.add('is-open');
        sidebar.classList.remove('-translate-x-full');
        sidebar.classList.add('translate-x-0');
        if (sidebarOverlay) {
            sidebarOverlay.classList.remove('hidden');
            sidebarOverlay.classList.add('is-visible');
        }
        document.body.style.overflow = 'hidden';
    }

    function closeSidebar() {
        if (!sidebar) return;
        sidebar.classList.remove('is-open');
        sidebar.classList.add('-translate-x-full');
        sidebar.classList.remove('translate-x-0');
        if (sidebarOverlay) {
            sidebarOverlay.classList.add('hidden');
            sidebarOverlay.classList.remove('is-visible');
        }
        document.body.style.overflow = '';
    }

    window.toggleSidebar = function () {
        if (!sidebar) return;
        if (sidebar.classList.contains('-translate-x-full')) {
            openSidebar();
        } else {
            closeSidebar();
        }
    };

    if (sidebarOpenBtn) {
        sidebarOpenBtn.addEventListener('click', openSidebar);
    }

    if (sidebarCloseBtn) {
        sidebarCloseBtn.addEventListener('click', closeSidebar);
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', closeSidebar);
    }

    // Close sidebar on Escape key
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeSidebar();
    });

    // Close sidebar on desktop resize
    window.addEventListener('resize', function () {
        if (window.innerWidth >= 1024) closeSidebar();
    });


    // ═══════════════════════════════════════
    // ACTIVE SIDEBAR LINK
    // ═══════════════════════════════════════

    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.sidebar-nav-link');

    navLinks.forEach(function (link) {
        const href = link.getAttribute('href');
        if (!href) return;

        // Exact match for dashboard, prefix match for other sections
        if (href === '/' && currentPath === '/') {
            link.classList.add('active');
        } else if (href !== '/' && currentPath.startsWith(href)) {
            link.classList.add('active');
        }
    });


    // ═══════════════════════════════════════
    // NOTIFICATION DROPDOWN
    // ═══════════════════════════════════════

    const notifBtn = document.getElementById('notification-button');
    const notifDropdown = document.getElementById('notification-dropdown');
    const notifBadge = document.getElementById('notif-badge');

    if (notifBtn && notifDropdown) {
        // Show badge if there are new notifications
        const currentCount = parseInt(notifBtn.getAttribute('data-notif-count')) || 0;
        const acknowledgedCount = parseInt(localStorage.getItem('acknowledged_notif_count')) || 0;

        if (currentCount > 0 && currentCount !== acknowledgedCount) {
            notifBadge.classList.add('is-visible');
        }

        // Toggle dropdown
        notifBtn.addEventListener('click', function (e) {
            e.stopPropagation();

            const isOpen = !notifDropdown.classList.contains('hidden');

            if (isOpen) {
                notifDropdown.classList.add('hidden', 'opacity-0', 'scale-95');
                notifDropdown.classList.remove('is-open', 'opacity-100', 'scale-100');
            } else {
                notifDropdown.classList.remove('hidden', 'opacity-0', 'scale-95');
                notifDropdown.classList.add('is-open', 'opacity-100', 'scale-100');

                // Acknowledge notifications
                if (currentCount > 0) {
                    localStorage.setItem('acknowledged_notif_count', currentCount);
                    if (notifBadge) notifBadge.classList.add('hidden');
                }
            }
        });

        // Close dropdown on outside click
        document.addEventListener('click', function (e) {
            if (!notifBtn.contains(e.target) && !notifDropdown.contains(e.target)) {
                notifDropdown.classList.add('hidden', 'opacity-0', 'scale-95');
                notifDropdown.classList.remove('is-open', 'opacity-100', 'scale-100');
            }
        });

        // Mark all as read
        const markAllReadBtn = document.getElementById('mark-all-read');
        const notifList = document.getElementById('notification-list');

        if (markAllReadBtn && notifList) {
            markAllReadBtn.addEventListener('click', function (e) {
                e.stopPropagation();
                notifList.innerHTML = '<div class="notif-empty">' +
                    '<div class="notif-empty-icon">' +
                    '<svg fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>' +
                    '</div>' +
                    '<p class="notif-empty-text">You\'re all caught up!</p>' +
                    '</div>';
                localStorage.setItem('acknowledged_notif_count', currentCount);
                notifBadge.classList.remove('is-visible');
            });
        }
    }


    // ═══════════════════════════════════════
    // TOAST AUTO-DISMISS
    // ═══════════════════════════════════════

    const toasts = document.querySelectorAll('.animate-toast');
    if (toasts.length > 0) {
        setTimeout(function () {
            toasts.forEach(function (toast) {
                toast.style.opacity = '0';
                toast.style.transform = 'translateY(-8px)';
                toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                setTimeout(function () { toast.remove(); }, 400);
            });
        }, 5000);
    }


    // ═══════════════════════════════════════
    // PAGE CONTENT ANIMATION
    // ═══════════════════════════════════════

    const pageContent = document.querySelector('.page-enter');
    if (pageContent) {
        pageContent.style.opacity = '0';
        requestAnimationFrame(function () {
            pageContent.style.opacity = '';
        });
    }

});
