# API Documentation: User Management System

**Version:** 2.1.0  
**Last Updated:** December 2024  
**Author:** Development Team  
**Status:** Production Ready

---

## Table of Contents

1. [Overview](#overview)
2. [Authentication](#authentication)
3. [Base URL and Versioning](#base-url-and-versioning)
4. [Rate Limiting](#rate-limiting)
5. [Error Handling](#error-handling)
6. [User Endpoints](#user-endpoints)
7. [Authentication Endpoints](#authentication-endpoints)
8. [Admin Endpoints](#admin-endpoints)
9. [Webhooks](#webhooks)
10. [SDKs and Libraries](#sdks-and-libraries)
11. [Examples](#examples)
12. [Changelog](#changelog)

---

## Overview

The User Management System API provides a comprehensive set of endpoints for managing user accounts, authentication, and authorization in your applications. This RESTful API follows industry standards and best practices for security, performance, and usability.

### Key Features

- **User Registration and Management**
- **JWT-based Authentication**
- **Role-based Access Control (RBAC)**
- **Password Reset and Email Verification**
- **Multi-factor Authentication (MFA)**
- **Audit Logging**
- **Real-time Webhooks**
- **Comprehensive Rate Limiting**

### Supported Formats

- **Request Format:** JSON
- **Response Format:** JSON
- **Date Format:** ISO 8601 (UTC)
- **Character Encoding:** UTF-8

---

## Authentication

### Bearer Token Authentication

All API requests require authentication using a Bearer token in the Authorization header:

```http
Authorization: Bearer <your_access_token>
```

### Token Types

| Token Type | Purpose | Lifetime | Refresh |
|------------|---------|----------|----------|
| **Access Token** | API access | 1 hour | Yes |
| **Refresh Token** | Token renewal | 30 days | No |
| **API Key** | Server-to-server | Permanent | No |

### Obtaining Tokens

```bash
# Login to get tokens
curl -X POST https://api.example.com/v2/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "secure_password"
  }'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "rt_1234567890abcdef",
  "token_type": "Bearer",
  "expires_in": 3600,
  "user": {
    "id": "usr_123456",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "user"
  }
}
```

---

## Base URL and Versioning

### Base URL

```
https://api.example.com/v2
```

### API Versioning

The API uses URL versioning. The current version is `v2`. Previous versions remain available:

- `v1` - Legacy (deprecated, sunset date: June 2025)
- `v2` - Current (recommended)

### Environment URLs

| Environment | Base URL |
|-------------|----------|
| **Production** | `https://api.example.com/v2` |
| **Staging** | `https://staging-api.example.com/v2` |
| **Development** | `https://dev-api.example.com/v2` |

---

## Rate Limiting

### Limits

| Plan | Requests/Hour | Burst Limit |
|------|---------------|-------------|
| **Free** | 1,000 | 100/min |
| **Pro** | 10,000 | 500/min |
| **Enterprise** | 100,000 | 2,000/min |

### Headers

Rate limit information is included in response headers:

```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
X-RateLimit-Window: 3600
```

### Rate Limit Exceeded

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 3600 seconds.",
    "details": {
      "limit": 1000,
      "window": 3600,
      "reset_at": "2024-01-01T12:00:00Z"
    }
  }
}
```

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| `200` | OK | Request successful |
| `201` | Created | Resource created successfully |
| `204` | No Content | Request successful, no content returned |
| `400` | Bad Request | Invalid request parameters |
| `401` | Unauthorized | Authentication required |
| `403` | Forbidden | Insufficient permissions |
| `404` | Not Found | Resource not found |
| `409` | Conflict | Resource already exists |
| `422` | Unprocessable Entity | Validation errors |
| `429` | Too Many Requests | Rate limit exceeded |
| `500` | Internal Server Error | Server error |
| `503` | Service Unavailable | Service temporarily unavailable |

### Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid parameters.",
    "details": {
      "field_errors": {
        "email": ["Email is required", "Email format is invalid"],
        "password": ["Password must be at least 8 characters"]
      }
    },
    "request_id": "req_123456789",
    "timestamp": "2024-01-01T12:00:00Z"
  }
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `INVALID_REQUEST` | Malformed request |
| `AUTHENTICATION_REQUIRED` | Missing or invalid authentication |
| `INSUFFICIENT_PERMISSIONS` | User lacks required permissions |
| `RESOURCE_NOT_FOUND` | Requested resource doesn't exist |
| `VALIDATION_ERROR` | Request validation failed |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Server-side error |

---

## User Endpoints

### Get Current User

Retrieve information about the authenticated user.

```http
GET /users/me
```

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "id": "usr_123456",
  "email": "user@example.com",
  "name": "John Doe",
  "avatar_url": "https://cdn.example.com/avatars/usr_123456.jpg",
  "role": "user",
  "permissions": ["read:profile", "write:profile"],
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "last_login": "2024-01-20T09:15:00Z",
  "email_verified": true,
  "mfa_enabled": false,
  "preferences": {
    "timezone": "UTC",
    "language": "en",
    "notifications": {
      "email": true,
      "push": false
    }
  }
}
```

### Update User Profile

Update the authenticated user's profile information.

```http
PATCH /users/me
```

**Request Body:**
```json
{
  "name": "John Smith",
  "preferences": {
    "timezone": "America/New_York",
    "language": "en",
    "notifications": {
      "email": true,
      "push": true
    }
  }
}
```

**Response:**
```json
{
  "id": "usr_123456",
  "email": "user@example.com",
  "name": "John Smith",
  "updated_at": "2024-01-20T14:30:00Z",
  "preferences": {
    "timezone": "America/New_York",
    "language": "en",
    "notifications": {
      "email": true,
      "push": true
    }
  }
}
```

### Change Password

Change the authenticated user's password.

```http
POST /users/me/password
```

**Request Body:**
```json
{
  "current_password": "old_password",
  "new_password": "new_secure_password",
  "confirm_password": "new_secure_password"
}
```

**Response:**
```json
{
  "message": "Password updated successfully",
  "password_changed_at": "2024-01-20T14:45:00Z"
}
```

### Upload Avatar

Upload a new avatar image for the authenticated user.

```http
POST /users/me/avatar
```

**Request:**
```http
Content-Type: multipart/form-data

--boundary
Content-Disposition: form-data; name="avatar"; filename="avatar.jpg"
Content-Type: image/jpeg

[binary image data]
--boundary--
```

**Response:**
```json
{
  "avatar_url": "https://cdn.example.com/avatars/usr_123456.jpg",
  "uploaded_at": "2024-01-20T15:00:00Z"
}
```

### Delete User Account

Permanently delete the authenticated user's account.

```http
DELETE /users/me
```

**Request Body:**
```json
{
  "password": "user_password",
  "confirmation": "DELETE"
}
```

**Response:**
```http
HTTP/1.1 204 No Content
```

---

## Authentication Endpoints

### Register User

Create a new user account.

```http
POST /auth/register
```

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "password": "secure_password",
  "name": "New User",
  "terms_accepted": true
}
```

**Response:**
```json
{
  "user": {
    "id": "usr_789012",
    "email": "newuser@example.com",
    "name": "New User",
    "email_verified": false,
    "created_at": "2024-01-20T16:00:00Z"
  },
  "message": "Registration successful. Please check your email to verify your account."
}
```

### Login

Authenticate a user and receive access tokens.

```http
POST /auth/login
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "user_password",
  "remember_me": true
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "rt_1234567890abcdef",
  "token_type": "Bearer",
  "expires_in": 3600,
  "user": {
    "id": "usr_123456",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "user"
  }
}
```

### Refresh Token

Refresh an expired access token using a refresh token.

```http
POST /auth/refresh
```

**Request Body:**
```json
{
  "refresh_token": "rt_1234567890abcdef"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Logout

Invalidate the current access token.

```http
POST /auth/logout
```

**Headers:**
```http
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "message": "Logged out successfully"
}
```

### Forgot Password

Initiate password reset process.

```http
POST /auth/forgot-password
```

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "message": "If an account with that email exists, a password reset link has been sent."
}
```

### Reset Password

Reset password using a reset token.

```http
POST /auth/reset-password
```

**Request Body:**
```json
{
  "token": "reset_token_123456",
  "new_password": "new_secure_password",
  "confirm_password": "new_secure_password"
}
```

**Response:**
```json
{
  "message": "Password reset successfully"
}
```

---

## Admin Endpoints

### List Users

Retrieve a paginated list of users (admin only).

```http
GET /admin/users?page=1&limit=20&sort=created_at&order=desc&search=john
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number |
| `limit` | integer | 20 | Items per page (max 100) |
| `sort` | string | created_at | Sort field |
| `order` | string | desc | Sort order (asc/desc) |
| `search` | string | - | Search term |
| `role` | string | - | Filter by role |
| `status` | string | - | Filter by status |

**Response:**
```json
{
  "users": [
    {
      "id": "usr_123456",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "user",
      "status": "active",
      "email_verified": true,
      "created_at": "2024-01-01T12:00:00Z",
      "last_login": "2024-01-20T09:15:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8,
    "has_next": true,
    "has_prev": false
  }
}
```

### Get User by ID

Retrieve detailed information about a specific user (admin only).

```http
GET /admin/users/{user_id}
```

**Response:**
```json
{
  "id": "usr_123456",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "status": "active",
  "email_verified": true,
  "mfa_enabled": false,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-15T10:30:00Z",
  "last_login": "2024-01-20T09:15:00Z",
  "login_count": 45,
  "preferences": {
    "timezone": "UTC",
    "language": "en"
  },
  "audit_log": [
    {
      "action": "login",
      "timestamp": "2024-01-20T09:15:00Z",
      "ip_address": "192.168.1.1",
      "user_agent": "Mozilla/5.0..."
    }
  ]
}
```

### Update User

Update a user's information (admin only).

```http
PATCH /admin/users/{user_id}
```

**Request Body:**
```json
{
  "name": "Updated Name",
  "role": "moderator",
  "status": "suspended",
  "email_verified": true
}
```

### Delete User

Permanently delete a user account (admin only).

```http
DELETE /admin/users/{user_id}
```

**Response:**
```http
HTTP/1.1 204 No Content
```

---

## Webhooks

### Overview

Webhooks allow your application to receive real-time notifications when certain events occur in the User Management System.

### Supported Events

| Event | Description |
|-------|-------------|
| `user.created` | New user registered |
| `user.updated` | User profile updated |
| `user.deleted` | User account deleted |
| `user.login` | User logged in |
| `user.logout` | User logged out |
| `user.password_changed` | User changed password |
| `user.email_verified` | User verified email |
| `user.suspended` | User account suspended |
| `user.reactivated` | User account reactivated |

### Webhook Payload

```json
{
  "id": "evt_123456789",
  "event": "user.created",
  "created_at": "2024-01-20T16:00:00Z",
  "data": {
    "user": {
      "id": "usr_789012",
      "email": "newuser@example.com",
      "name": "New User",
      "role": "user",
      "created_at": "2024-01-20T16:00:00Z"
    }
  },
  "metadata": {
    "ip_address": "192.168.1.1",
    "user_agent": "Mozilla/5.0..."
  }
}
```

### Webhook Security

Webhooks are signed using HMAC-SHA256. Verify the signature using the `X-Webhook-Signature` header:

```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(f"sha256={expected_signature}", signature)
```

---

## SDKs and Libraries

### Official SDKs

| Language | Package | Documentation |
|----------|---------|---------------|
| **JavaScript/Node.js** | `@example/user-api` | [Docs](https://docs.example.com/sdk/js) |
| **Python** | `example-user-api` | [Docs](https://docs.example.com/sdk/python) |
| **PHP** | `example/user-api` | [Docs](https://docs.example.com/sdk/php) |
| **Ruby** | `example-user-api` | [Docs](https://docs.example.com/sdk/ruby) |
| **Go** | `github.com/example/user-api-go` | [Docs](https://docs.example.com/sdk/go) |

### JavaScript SDK Example

```javascript
import { UserAPI } from '@example/user-api';

const api = new UserAPI({
  apiKey: 'your_api_key',
  baseURL: 'https://api.example.com/v2'
});

// Get current user
const user = await api.users.me();
console.log(user.name);

// Update user profile
const updatedUser = await api.users.update({
  name: 'New Name',
  preferences: {
    timezone: 'America/New_York'
  }
});
```

### Python SDK Example

```python
from example_user_api import UserAPI

api = UserAPI(
    api_key='your_api_key',
    base_url='https://api.example.com/v2'
)

# Get current user
user = api.users.me()
print(user.name)

# Update user profile
updated_user = api.users.update(
    name='New Name',
    preferences={
        'timezone': 'America/New_York'
    }
)
```

---

## Examples

### Complete Registration Flow

```javascript
// 1. Register new user
const registerResponse = await fetch('https://api.example.com/v2/auth/register', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'secure_password',
    name: 'John Doe',
    terms_accepted: true
  })
});

const registerData = await registerResponse.json();
console.log('User registered:', registerData.user.id);

// 2. User verifies email (handled by email link)

// 3. Login after verification
const loginResponse = await fetch('https://api.example.com/v2/auth/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'secure_password'
  })
});

const loginData = await loginResponse.json();
const accessToken = loginData.access_token;

// 4. Use access token for API calls
const userResponse = await fetch('https://api.example.com/v2/users/me', {
  headers: {
    'Authorization': `Bearer ${accessToken}`
  }
});

const userData = await userResponse.json();
console.log('Current user:', userData);
```

### Error Handling Example

```javascript
async function apiCall(url, options = {}) {
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
        ...options.headers
      },
      ...options
    });

    if (!response.ok) {
      const errorData = await response.json();
      
      switch (response.status) {
        case 401:
          // Token expired, refresh it
          await refreshToken();
          return apiCall(url, options); // Retry
          
        case 429:
          // Rate limited, wait and retry
          const retryAfter = response.headers.get('Retry-After') || 60;
          await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
          return apiCall(url, options); // Retry
          
        case 422:
          // Validation errors
          throw new ValidationError(errorData.error.details.field_errors);
          
        default:
          throw new APIError(errorData.error.message, response.status);
      }
    }

    return await response.json();
  } catch (error) {
    console.error('API call failed:', error);
    throw error;
  }
}
```

### Pagination Example

```python
def get_all_users(api):
    """Get all users using pagination"""
    all_users = []
    page = 1
    
    while True:
        response = api.admin.users.list(
            page=page,
            limit=100
        )
        
        all_users.extend(response['users'])
        
        if not response['pagination']['has_next']:
            break
            
        page += 1
    
    return all_users
```

---

## Changelog

### Version 2.1.0 (December 2024)

**New Features:**
- Added multi-factor authentication (MFA) support
- Introduced webhook system for real-time notifications
- Added user preferences management
- Implemented audit logging for admin actions

**Improvements:**
- Enhanced rate limiting with burst protection
- Improved error messages with detailed field validation
- Added support for avatar uploads
- Optimized pagination performance

**Bug Fixes:**
- Fixed token refresh race condition
- Resolved email verification edge cases
- Fixed timezone handling in date responses

### Version 2.0.0 (September 2024)

**Breaking Changes:**
- Migrated from API v1 to v2
- Changed authentication from API keys to JWT tokens
- Updated response format for consistency
- Removed deprecated endpoints

**New Features:**
- JWT-based authentication
- Role-based access control (RBAC)
- Enhanced user profile management
- Comprehensive admin endpoints

### Version 1.2.0 (June 2024)

**New Features:**
- Added password reset functionality
- Implemented email verification
- Added user search and filtering

**Improvements:**
- Enhanced security with password hashing
- Improved API documentation
- Added rate limiting

---

## Support

### Getting Help

- **Documentation:** [https://docs.example.com](https://docs.example.com)
- **API Status:** [https://status.example.com](https://status.example.com)
- **Support Email:** api-support@example.com
- **Community Forum:** [https://community.example.com](https://community.example.com)

### SLA and Uptime

- **Uptime Guarantee:** 99.9%
- **Response Time:** < 200ms (95th percentile)
- **Support Response:** < 24 hours

### Security

To report security vulnerabilities, please email security@example.com with details. We follow responsible disclosure practices and will acknowledge receipt within 24 hours.

---

**© 2024 Example Company. All rights reserved.**