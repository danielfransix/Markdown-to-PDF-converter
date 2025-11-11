# Table Examples

This document demonstrates various table formatting options and how they appear in PDF output.

## Basic Tables

### Simple Table

| Name | Age | City |
|------|-----|------|
| John | 25 | New York |
| Jane | 30 | London |
| Bob | 35 | Paris |

### Table with Alignment

| Left Aligned | Center Aligned | Right Aligned |
|:-------------|:--------------:|--------------:|
| Left | Center | Right |
| This text is left aligned | This text is centered | This text is right aligned |
| Short | Medium length text | Very long text that might wrap |

## Advanced Tables

### Table with Formatting

| Feature | **Status** | *Priority* | `Code` |
|---------|------------|------------|---------|
| Authentication | ✅ **Complete** | *High* | `auth.js` |
| Database | 🔄 *In Progress* | *Medium* | `db.py` |
| UI Design | ❌ **Pending** | *Low* | `styles.css` |
| Testing | ⚠️ *Partial* | *High* | `test.js` |

### Product Comparison Table

| Product | Price | Features | Rating | Availability |
|---------|-------|----------|--------|--------------|
| **Basic Plan** | $9.99/month | • 10GB Storage<br>• Email Support<br>• Basic Analytics | ⭐⭐⭐ | ✅ Available |
| **Pro Plan** | $19.99/month | • 100GB Storage<br>• Priority Support<br>• Advanced Analytics<br>• API Access | ⭐⭐⭐⭐ | ✅ Available |
| **Enterprise** | $49.99/month | • Unlimited Storage<br>• 24/7 Phone Support<br>• Custom Analytics<br>• Full API Access<br>• White-label Options | ⭐⭐⭐⭐⭐ | 📞 Contact Sales |

## Data Tables

### Financial Data

| Quarter | Revenue | Expenses | Profit | Growth |
|---------|--------:|---------:|-------:|-------:|
| Q1 2023 | $125,000 | $95,000 | $30,000 | +15% |
| Q2 2023 | $142,000 | $98,000 | $44,000 | +47% |
| Q3 2023 | $158,000 | $102,000 | $56,000 | +27% |
| Q4 2023 | $175,000 | $108,000 | $67,000 | +20% |
| **Total** | **$600,000** | **$403,000** | **$197,000** | **+27%** |

### Technical Specifications

| Component | Specification | Performance | Notes |
|-----------|---------------|-------------|-------|
| **CPU** | Intel i7-12700K | 3.6 GHz Base<br>5.0 GHz Boost | 12 cores, 20 threads |
| **RAM** | DDR4-3200 | 32GB | 2x16GB modules |
| **Storage** | NVMe SSD | 1TB | PCIe 4.0 |
| **GPU** | RTX 4070 | 12GB VRAM | Ray tracing support |
| **PSU** | 750W Gold | 80+ Certified | Modular cables |

## Complex Tables

### Project Timeline

| Phase | Task | Start Date | End Date | Duration | Assigned To | Status |
|-------|------|------------|----------|----------|-------------|--------|
| **Phase 1** | Requirements Gathering | 2024-01-01 | 2024-01-15 | 2 weeks | *Project Manager* | ✅ Complete |
| | Stakeholder Interviews | 2024-01-08 | 2024-01-22 | 2 weeks | *Business Analyst* | ✅ Complete |
| **Phase 2** | System Design | 2024-01-16 | 2024-02-05 | 3 weeks | *Lead Architect* | ✅ Complete |
| | Database Design | 2024-01-23 | 2024-02-12 | 3 weeks | *Database Admin* | 🔄 In Progress |
| **Phase 3** | Frontend Development | 2024-02-06 | 2024-03-19 | 6 weeks | *Frontend Team* | 📅 Scheduled |
| | Backend Development | 2024-02-13 | 2024-03-26 | 6 weeks | *Backend Team* | 📅 Scheduled |
| **Phase 4** | Testing & QA | 2024-03-20 | 2024-04-16 | 4 weeks | *QA Team* | ⏳ Pending |
| | Deployment | 2024-04-17 | 2024-04-30 | 2 weeks | *DevOps Team* | ⏳ Pending |

### API Endpoints

| Method | Endpoint | Description | Parameters | Response |
|--------|----------|-------------|------------|----------|
| `GET` | `/api/users` | Get all users | `?page=1&limit=10` | `200 OK`<br>`{ "users": [...] }` |
| `GET` | `/api/users/{id}` | Get user by ID | `id` (path parameter) | `200 OK`<br>`{ "user": {...} }` |
| `POST` | `/api/users` | Create new user | `{ "name": "...", "email": "..." }` | `201 Created`<br>`{ "user": {...} }` |
| `PUT` | `/api/users/{id}` | Update user | `id` (path)<br>`{ "name": "...", "email": "..." }` | `200 OK`<br>`{ "user": {...} }` |
| `DELETE` | `/api/users/{id}` | Delete user | `id` (path parameter) | `204 No Content` |

## Table Styling Tips

### Best Practices

| Practice | Description | Example |
|----------|-------------|----------|
| **Use Headers** | Always include descriptive headers | ✅ `| Name | Age |` |
| **Consistent Alignment** | Align similar data types consistently | Numbers: right-aligned |
| **Readable Width** | Keep columns at reasonable widths | Avoid very long text |
| **Visual Hierarchy** | Use formatting to show importance | **Bold** for totals |
| **Clear Separators** | Use proper spacing and borders | Clean table structure |

### Common Mistakes

| ❌ Mistake | ✅ Better Approach | Why |
|------------|-------------------|-----|
| No headers | Include descriptive headers | Improves readability |
| Inconsistent alignment | Use consistent alignment rules | Looks more professional |
| Too much text in cells | Keep cells concise, use line breaks | Easier to scan |
| No visual hierarchy | Use formatting for emphasis | Highlights important data |
| Poor spacing | Proper column widths | Better visual balance |

## Conclusion

Tables are powerful tools for presenting structured data in documents. The PDF converter should maintain table formatting, alignment, and styling while ensuring readability across different page sizes.

**Key Points**:
- Use appropriate alignment for different data types
- Include clear, descriptive headers
- Apply consistent formatting throughout
- Consider the visual hierarchy of information
- Keep table content concise and scannable