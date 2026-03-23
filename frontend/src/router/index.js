// import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/Home.vue'
// import Privacy from '../components/Privacy.vue' // Ensure this path is correct
// import Terms from '../components/Terms.vue'
// import TrainBooking from '../components/Train-booking.vue'
// import Guide from '../components/Guide.vue'
// import CustomItinerary from '../components/Custom-Itinerary.vue'
// import TravelInsurance from '../components/TravelInsurance.vue'
// import Uhome from '../views/Uhome.vue'
// import Uprofile from '../components/Uprofile.vue'
// import Ubookings from '../components/Ubookings.vue'
// import Usopports from '../components/Usopports.vue'
// import Ahome from '../views/Ahome.vue'
// import Asecurity from '../components/Asecurity.vue'
// import Asystemlog from '../components/Asystemlog.vue'

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: Home,
//   },
//   {
//     path: '/privacy',
//     name: 'Privacy',
//     component: Privacy,
//   },
//   {
//     path: '/terms',
//     name: 'Terms',
//     component: Terms,
//   },
//   {
//     path: '/train-booking',
//     name: 'TrainBooking',
//     component: TrainBooking,
//   },
//   { 
//     path: '/guide', 
//     name: 'Guide', 
//     component: Guide 
//   },
//   { 
//     path: '/custom-itinerary', 
//     name: 'CustomItinerary', 
//     component: CustomItinerary 
//   },
//   {
//     path: '/travel-insurance',
//     name: 'TravelInsurance',
//     component: TravelInsurance,
//   },
//   {
//     path: '/uhome',
//     name: 'Uhome',
//     component: Uhome,
//   },
//   {
//     path: '/uprofile',
//     name: 'Uprofile',
//     component: Uprofile,
//   },
//   {
//     path: '/ubookings',
//     name: 'Ubookings',
//     component: Ubookings,
//   },
//   {
//     path: '/usopports',
//     name: 'Usopports',
//     component: Usopports,
//   },
//   {
//     path: '/ahome',
//     name: 'Ahome',
//     component: Ahome,
//   },
//   {
//     path: '/asecurity',
//     name: 'Asecurity',
//     component: Asecurity,
//   },
//   {
//     path: '/asystemlog',
//     name: 'Asystemlog',
//     component: Asystemlog,
//   },

// ]

// export default createRouter({
//   history: createWebHistory(),
//   routes,
//   // Added scrollBehavior to ensure page starts at the top when navigating
//   scrollBehavior() {
//     return { top: 0 }
//   }
// })









import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Privacy from '../components/Privacy.vue' 
import Terms from '../components/Terms.vue'
import TrainBooking from '../components/Train-booking.vue'
import Guide from '../components/Guide.vue'
import CustomItinerary from '../components/Custom-Itinerary.vue'
import TravelInsurance from '../components/TravelInsurance.vue'

// User Dashboard Components
import Uhome from '../views/Uhome.vue'
import Uprofile from '../components/Uprofile.vue'
import Ubookings from '../components/Ubookings.vue'
import Usopports from '../components/Usopports.vue'

// Admin Dashboard Components
import Ahome from '../views/Ahome.vue'
import Asecurity from '../components/Asecurity.vue'
import Asystemlog from '../components/Asystemlog.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/privacy', name: 'Privacy', component: Privacy },
  { path: '/terms', name: 'Terms', component: Terms },
  { path: '/train-booking', name: 'TrainBooking', component: TrainBooking },
  { path: '/guide', name: 'Guide', component: Guide },
  { path: '/custom-itinerary', name: 'CustomItinerary', component: CustomItinerary },
  { path: '/travel-insurance', name: 'TravelInsurance', component: TravelInsurance },

  // --- USER ROUTES ---
  {
    path: '/uhome',
    name: 'Uhome',
    component: Uhome,
    meta: { requiresAuth: true, role: 'User' }
  },
  {
    path: '/uprofile',
    name: 'Uprofile',
    component: Uprofile,
    meta: { requiresAuth: true, role: 'User' }
  },
  {
    path: '/ubookings',
    name: 'Ubookings',
    component: Ubookings,
    meta: { requiresAuth: true, role: 'User' }
  },
  {
    path: '/usopports',
    name: 'Usopports',
    component: Usopports,
    meta: { requiresAuth: true, role: 'User' }
  },

  // --- ADMIN ROUTES (Fixed with allowedRoles) ---
  {
    path: '/ahome',
    name: 'Ahome',
    component: Ahome,
    meta: { requiresAuth: true, allowedRoles: ['SuperAdmin', 'Manager', 'Support'] }
  },
  {
    path: '/asecurity',
    name: 'Asecurity',
    component: Asecurity,
    meta: { requiresAuth: true, allowedRoles: ['SuperAdmin'] }
  },
  {
    path: '/asystemlog',
    name: 'Asystemlog',
    component: Asystemlog,
    meta: { requiresAuth: true, allowedRoles: ['SuperAdmin', 'Manager'] }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

/**
 * UPDATED Navigation Guard for Multi-Role Support
 */
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('user_token');
  const rawData = localStorage.getItem('user_data');
  
  let userRole = null;

  if (rawData) {
    try {
      const userData = JSON.parse(rawData);
      userRole = userData.role; 
    } catch (e) {
      userRole = null;
    }
  }

  // 1. Check if route requires authentication
  if (to.meta.requiresAuth) {
    // No token? Send to Home/Login
    if (!token) {
      return next({ name: 'Home' });
    }

    // 2. Handle Admin Routes (Array Check)
    if (to.meta.allowedRoles) {
      if (!to.meta.allowedRoles.includes(userRole)) {
        alert("Access Denied: Your role does not have permission for this section.");
        // If they are an admin but not SuperAdmin, send them to Ahome
        return next(userRole === 'User' ? { name: 'Uhome' } : { name: 'Ahome' });
      }
    }

    // 3. Handle User Routes (Single String Check)
    if (to.meta.role && to.meta.role !== userRole) {
      if (userRole === 'SuperAdmin' || userRole === 'Manager' || userRole === 'Support') {
        return next({ name: 'Ahome' });
      } else {
        return next({ name: 'Home' });
      }
    }
  }

  next();
})

export default router